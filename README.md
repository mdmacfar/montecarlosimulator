# Monte Carlo Simulator Module
Author: Michael Macfarlan

## Synopsis 
Show demo code of how the classes are used, i.e.installing importing Creating dice Playing games Analyzing games. 

## API Description 
A list of all classes with their public methods and attributes. 
Each item should show their docstrings. 
All paramters (with data types and defaults) should be described. 
All return values should be described. Do not describe private methods and attributes. 

## Manifest 
Here is what you'll find in the repo:

- montecarlosimulatormodule/
  - README.md
  - setup.py
  - mcsmod/
    - __init__.py
    - montecarlo.py
    - tests/
      - __init__.py
      - mcstest.py


## Instructions 

Remember to run

pip install -e . 

from the directory that the setup.py file is in. 

Then to run the unit test, run 

python -m unittest discover mcsmod/tests > test_output.txt

This will overwrite the test_output.txt file.