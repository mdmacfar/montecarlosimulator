import pandas as pd
import random
from typing import List

class Die:
    """
    This class represents a die. 

    Attributes:
    faces: An array of die faces
    weights: An array of weights for each of the faces

    Methods:
    __init__(self, faces): Initializes a new Die object.
    change_weight(self, face, weight): Changes the weight of a side of the die.
    roll(self, times=1): Rolls the die.
    show(self): Shows the die's current set of faces and weights.

    """

    def __init__(self, faces):
        """
        Initializes a new Die object.

        Parameters:
        faces: An array of die faces

        """
        self.faces = faces
        self.weights = [1.0] * len(faces)
        self.dataframe = pd.DataFrame({'faces': self.faces, 'weight': self.weights})

    def change_weight(self, face, weight):
        """
        Changes the weight of a side of the die.

        Parameters:
        face: The face to change the weight of.
        weight: The new weight of the face.

        """
        if face not in self.faces:
            raise ValueError("Face not found in die.")
        try:
            weight=float(weight)
        except ValueError:
            raise ValueError("Weight must be a number.")
        self.weights[self.faces.index(face)] = weight
        self.dataframe = pd.DataFrame({'faces': self.faces, 'weight': self.weights})

    def roll(self, times=1):
        """
        Rolls the die.

        Parameters:
        times: Number of times to roll the die. Default is 1.

        """
        results = []
        for i in range(times):
            results.append(random.choices(self.faces, weights=self.weights)[0])
        return results
    
    def show(self):
        """
        Shows the die's current set of faces and weights.

        """
        print(self.dataframe)

class Game:
    """
    This class represents a game of rolling dice.

    Attributes:
    dice: A list of die objects
    results: A datafame of the results of the rolls

    Methods:
    __init__(self, dice: List[Die]): Initializes a new Game object.
    play(self, times=int): Plays the game for a certain number of times.
    show(self, wide: bool=True): Shows the results of the last play.

    """
    def __init__(self, dice: List[Die]):
        """
        Initializes a new Game object.

        Parameters:
        dice: A list of die objects

        """
        self.dice = dice
        self.results = pd.DataFrame()

    def play(self, times=int):
        """
        Plays the game for a certain number of times.

        Parameters:
        times: Number of times to play the game.

        """
        results = []
        for i in range(times):
            roll = [die.roll()[0] for die in self.dice]
            results.append(roll)
        cols = [f'die_{i+1}' for i in range(len(self.dice))]
        self.results = pd.DataFrame(results, columns=cols)

    def show(self, wide: bool=True):
        """
        Shows the results of the last play.

        Parameters:
        wide: Whether to show the results in wide format (default) or narrow format.

        """
        if self.results is None:
            print("No results to show.")
            return
        
        if wide:
            print(self.results)

        else:
            narrow = pd.melt(self.results, var_name='die', value_name='result')
            narrow['roll'] = narrow.index
            narrow = narrow[['roll', 'die', 'result']]
            print(narrow)


class Analyzer:
    """
    Takes the results of a game and computes statistical properties. 
    The property results are available as attributes of the Analyzer object.

    Attributes:
    count_faces: How many times a given face appears in the results.
    count_jackpots: How many times all the faces are the same.
    count_combos: How many times a given combination of faces appears in the results.


    """
    def __init__(self, game: Game):
        """
        Initializes a new Analyzer object.

        Parameters:
        game: A Game object to analyze.
        """

        self.game = game
        self.faces_dtype = self.get_faces_dtype()
        self.face_count_results = None
        self.jackpot_results = None
        self.combo_results = None
        

    def get_faces_dtype(self):
        """
        Gets the data type of the faces in the results.

        """
        dtypes = set()
        for die in self.game.dice:
            dtype=str(type(die.faces[0]))
            if dtype not in ["<class 'str'>", "<class 'int'>", "<class 'float'>"]:
                raise TypeError("Faces must be strings, integers, or floats.")
            dtypes.add(dtype)

        if len(dtypes) > 1:
            raise TypeError("All die must have the same face type (string, integer, or float).")
        
        if "<class 'str'>" in dtypes:
            return 'str'
        elif "<class 'int'>" in dtypes:
            return 'int'
        elif "<class 'float'>" in dtypes:
            return 'float'


    def count_faces(self):
        """
        How many times a given face appears in the results.

        """
        faces_count_dict = {}
        for face in self.game.dice[0].faces:
            faces_count_dict[face] = self.game.results.apply(lambda row: (row == face).sum(), axis=1).sum()
        self.face_count_results = pd.DataFrame.from_dict(faces_count_dict, orient='index', columns=['count'])
        self.face_count_results.index.name = 'face'
        return self.face_count_results
        
    def count_jackpots(self):
        """
        How many times all the faces are the same.

        """
        jackpots = self.game.results.apply(lambda row: len(set(row)) == 1, axis=1)
        self.jackpot_results = pd.DataFrame({'jackpot': jackpots, 'count':1}).groupby('jackpot').sum()
        self.jackpot_results.index = pd.Categorical(['no_jackpot', 'jackpot'], ordered=True)
        return self.jackpot_results
        
    def count_combos(self, combo: List):
        """
        Counts how many times a given combination of faces appears in the results.

        Parameters:
        combo: A list of faces to count.

        """

        combo_count = self.game.results.apply(lambda row: set(combo).issubset(set(row)), axis=1).sum()
        combo_str = ", ".join(map(str, combo))
        self.combo_results = pd.DataFrame({'combo': [combo_str], 'count': [combo_count]})
        return self.combo_results