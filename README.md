# Monte Carlo Simulator
Author: Michael Macfarlan

## Synopsis 

🎲🎲🎲 _They see me rollin'_ 🎲🎲🎲

This Monte Carlo Simulation package is a Python library designed to simulate and analyze games of randomly rolled dice. With this tool, you can create different kinds of dice with different weights, play games with dice, and analyze the outcomes of games. The package is easy to use with clear instructions (see the bottom of this README file) and useful demos (see the notebook titled "montecarlo_demo.ipynb"). 

### Example:
```
from mcs_pkg.montecarlo import Die, Game, Analyzer

# Setup: A fair coin (with faces H and T) and one unfair coin, 
# in which one of the faces has a weight of 5 and the others 1.

fair_coin = Die(['H', 'T'])
unfair_coin = Die(['H', 'T'])
unfair_coin.change_weight('H', 5)

# Here's a game of 1000 flips with two fair coins

fairgame = Game([fair_coin, fair_coin])
fairgame.play(1000)

# Now, we analyze the frequency of jackpots 
# during the game played with fair coins

fairgame_analyzer = Analyzer(fairgame)
fairgame_jackpot = fairgame_analyzer.count_jackpots()
fairgame_flips = fairgame.results.shape[0]
fairgame_jackpot
fairgame_flips
fairgame_freq = fairgame_jackpot / fairgame_flips
print(fairgame_freq)

```
See the __montecarlo_demo.ipynb__ file for more examples and scenarios.

## API Description 

Classes: 

### Die Class:
This class represents a die. 
<br>Attributes:
<br>faces: An array of die faces
<br>weights: An array of weights for each of the faces

Methods:
<br>`__init__(self, faces)`: Initializes a new Die object.<br>`change_weight(self, face, weight)`: Changes the weight of a side of the die.
<br>`roll(self, times=1)`: Rolls the die.
<br>`show(self)`: Shows the die's current set of faces and weights.

### Game Class:
This class represents a game of rolling dice.
<br>Attributes:
<br>dice: A list of die objects
<br>results: A datafame of the results of the rolls

Methods:
<br>`__init__(self, dice: List[Die])`: Initializes a new Game object.
<br>`play(self, times=int)`: Plays the game for a certain number of times.
<br>`show(self, wide: bool=True)`: Shows the results of the last play.

### Analyzer Class:
Takes the results of a game and computes statistical properties. The results are available to use as attributes of the Analyzer object.

Attributes:
<br>`count_faces`: Count how many times a given face appears in the results.
<br>`count_jackpots`: Count how many times all the faces are the same.
<br>`count_combos`: Count how many times a given combination of faces appears in the results.


## Manifest 
Here is what you'll find in the repo:

- montecarlosimulator/
  - README.md (This file)
  - License (The license)
  - setup.py (Setup file for the package installation)
  - montecarlo_tests_results.txt (Unit test output)
  - scratch.py (A place to run manual mini tests)
  - montecarlo_demo.ipynb (A jupyter notebook to run different scenarios)
  - tests/
    - montecarlo_tests.py (Unit test file)
  - mcs_pkg/
    - __init__.py (Package initializer)
    - montecarlo.py (The juicy bits of the package)

## General Installation Instructions

Instructions to install:

1. Make sure you have Python, Pip, Pandas, and Matplotlib installed in your environment.
  
2. Copy the repo to your environment, then run these bash commands from the same directory as your repo:
  
  ```pip install -e . && python3 -m mcs_pkg ```

3. You're ready to use the package. Experiment with different scenarios by opening __montecarlo_demo.ipynb__ and running the cells
  
4. To run the Unit test, run:

  ```python3 -m unittest discover tests 2> montecarlo_tests_results.txt```
  
This will overwrite the montecarlo_tests_results.txt file with a new output.


## Installation Instructions For Docker Dev Environment

Instructions to install within a Docker environment:

1. Start a dev environment from Docker desktop. When prompted, use https://github.com/mdmacfar/montecarlosimulator.git to install the environment.
2. Open VSCode from Docker when prompted. Open a terminal (Terminal > New Terminal)
3. In the terminal, run:
  
  ```sudo apt-get update && sudo apt-get install -y python3-pip && pip3 install pandas && pip3 install matplotlib && pip install -e . && python3 -m mcs_pkg ```

4. You're ready to use the package. Experiment with different scenarios by opening __montecarlo_demo.ipynb__ and running the cells
  
5. To run the Unit test, run:

  ```python3 -m unittest discover tests 2> montecarlo_tests_results.txt```
  
This will overwrite the montecarlo_tests_results.txt file with a new output.

Enjoy!