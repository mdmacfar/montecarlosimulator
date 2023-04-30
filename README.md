# Monte Carlo Simulator
Author: Michael Macfarlan

## Synopsis 
Show demo code of how the classes are used, i.e.installing importing Creating dice Playing games Analyzing games. 

## API Description 

Classes: 

### class Die:
This class represents a die. 
Attributes:
faces: An array of die faces
weights: An array of weights for each of the faces

Methods:
__init__(self, faces): Initializes a new Die object.
change_weight(self, face, weight): Changes the weight of a side of the die.
roll(self, times=1): Rolls the die.
show(self): Shows the die's current set of faces and weights.

### class Game:
This class represents a game of rolling dice.
Attributes:
dice: A list of die objects
results: A datafame of the results of the rolls

Methods:
__init__(self, dice: List[Die]): Initializes a new Game object.
play(self, times=int): Plays the game for a certain number of times.
show(self, wide: bool=True): Shows the results of the last play.

### class Analyzer:
Takes the results of a game and computes statistical properties. 
The property results are available as attributes of the Analyzer object.

Attributes:
count_faces: How many times a given face appears in the results.
count_jackpots: How many times all the faces are the same.
count_combos: How many times a given combination of faces appears in the results.


## Manifest 
Here is what you'll find in the repo:

- montecarlosimulator/
  - README.md (This file)
  - License (The license)
  - setup.py (Setup file for the package installation)
  - test_mcs_results.txt (Unit test output)
  - scratch.py (A place to run manual mini tests)
  - demoscenarios.ipynb (A jupyter notebook to run different scenarios)
  - tests/
    - test_mcs.py (Unit test file)
  - mcs_pkg/
    - __init__.py (Package initializer)
    - montecarlo.py (The juicy bits of the package)



## Instructions 

Instructions to install within a Docker environment:

1. Start a dev environment from Docker desktop. When prompted, use https://github.com/mdmacfar/montecarlosimulator.git to install the environment.
2. Open VSCode from Docker when prompted. Open a terminal (Terminal > New Terminal)
3. In the terminal, run:
  
  ```sudo apt-get update && sudo apt-get install -y python3-pip```
  
4. Then run:

```pip3 install pandas```
  
  ```pip3 install matplotlib #(this is for the jupyter notebook graphs)```
  
  ```pip install -e .```
  
  ```python3 -m mcs_pkg ```
  
5. To run the Unit test, run:

  ```python3 -m unittest discover tests 2> test_mcs_results.txt```
  
This will overwrite the test_mcs_results.txt file with a new output.
