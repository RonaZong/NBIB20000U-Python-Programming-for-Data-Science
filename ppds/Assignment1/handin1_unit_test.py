import os

from io import StringIO
import sys

def parse_per_block(filename):
    '''parse a shell script file into individual commands'''
    script_file = open(filename)

    commands_list = [[]]
    current_commands = []
    for line in script_file:
        line = line.rstrip()

        # Split on new lines - register only if command is not empty
        if line == "" and len(commands_list[-1]) > 0:
            commands_list.append([])
        elif line != "":
            commands_list[-1].append(line)

    print(commands_list)
    return commands_list

def exec_python(python_line_list):
    '''eval python code lines - one at a time - and collect output'''
    # print("Evaluating: ", python_line_list)
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    output = exec("\n".join(python_line_list), globals())
    sys.stdout = old_stdout
    return (output, mystdout.getvalue())

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.python_line_block_list = parse_per_block('handin1.py')

def teardown_module(module):
    """Make sure process is dead"""
    pass

def test_python_ex1():
    '''Test reading of content into list'''
    exec_python(python_line_block_list[0])
    # Check for book_file variable name
    assert('lines' in globals())
    # Check that book_file is of type list
    assert(isinstance(globals()['lines'], list))

def test_python_ex2():
    '''Test counting lines'''
    output = exec_python(python_line_block_list[1])[1].strip()
    correct_length = "3736"
    assert(output == correct_length)

def test_python_ex3():
    '''Test printing of 41st line'''
    output = exec_python(python_line_block_list[2])[1].strip()
    correct_line = "CHAPTER I. Down the Rabbit-Hole"
    assert(output == correct_line)

def test_python_ex4():
    '''Test counting words in of 43rd line'''
    output = exec_python(python_line_block_list[3])[1].strip()
    correct_count = "14"
    assert(correct_count == output)
    
def test_python_ex5():
    '''Test for correct lines in junk output file'''
    exec_python(python_line_block_list[4])
    assert(os.path.exists("junk.txt"))
    with open("junk.txt") as junk_file:
        junk_content = junk_file.readlines()
    assert(junk_content == ["Title: Alice's Adventures in Wonderland\n", "\n", "Author: Lewis Carroll\n"])
