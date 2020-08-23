 import pytest
import random
import string
import session6
import os
import inspect
import re
import math, cmath
from timeit import default_timer as timer

SIDES = random.choice([3, 4, 5, 6])
LENGTH = random.randint(1, 100)
TEMP = random.uniform(-100, 100)
NUMBER = 5
RANDOM_NUMBER = random.randint(1, 20)
START = random.randint(1, 10)
END = random.randint(11, 20)
SPEED = random.uniform(1, 100)

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter', 
]

#1
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

#2
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

#3
def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

#4    
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

#5
def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

#6
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#7		
def test_functions_list():
    code_lines = inspect.getsource(session6)
    assert 'time_it' in code_lines, 'time_it function is not present'
    assert 'squared_power_list' in code_lines, 'squared_power_list function is not present'
    assert 'temp_converter' in code_lines, 'temp_converter function is not present'
    assert 'polygon_area' in code_lines, 'polygon_area function is not present'
    assert 'speed_converter' in code_lines, 'speed_converter function is not present'
