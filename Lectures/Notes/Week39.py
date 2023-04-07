# Import modules
import module_name
from module_name import names
from module_name import *

import sys
print(sys.path)

# Import package
import Bio.PDB.PDBParser

# Regular Expressions
. # Match any character
a # Match 'a' (normal text)
ab # Match 'a' followed by 'b' (normal text)
[abc] # Character class. Match one character: either 'a' or 'b' or 'c'
[^abc] # Character class. Match one character: anything except 'a' or 'b' or 'c'
[a-z] # Character class. Match one character: anything between 'a' and 'z'
^ and $ # Matches beginning and end of line
\A and \Z # Matches beginning and end of entire string

* # zero or more times
+ # one or more times
? # zero or one time
{n} # n times
{n,} # at least n times
{,n} # at most n times
{n,m} # between n and m times

# Non-greedy Repetition
*? # Match zero or more times
+? # Match one ore more times
?? # Match zero or one time
{n}? # Match n times
{n,}? # Match at least n times
{,n}? # Match at most n times
{n,m}? # Match between n and m times

(expr) # Group an expression
(expr1|expr2) # Match either expr1 or expr2
\. # Matches a literal '.' (escaping)
\? # Matches a literal '?' (escaping)


# Special Characters
\d # digital character [0-9]
\D # non-digital character [^0-9]
\w # alphanumerical character [a-zA-Z0-9_]
\W # non-alphanumerical character [^a-zA-Z0-9_]
\s # white-space character [\t\n\r\f\v]
\S # non-white-space character [^\t\n\r\f\v]

# Boundaries
^ and $ # Matches beginning and end of line
\A and \Z # Matches beginning and end of entire string
\b # Match at boundary of word
\B # Match anywhere except at boundary of word
# \ also means backspace in python, therefore,
# \\b to escape the backslash,
r # Use raw strings to write RE

\1 \2 # Reffer to groups matched in a previous part of an expression

# Import regular expressions
import re
re.compile() # One or more characters between a-z and A-Z
re.match() # Check whether the pattern matches from start of the string. Returns match object
re.search() # Search for substrings where pattern matches. Returns match object
re.findall() # Search for substrings where pattern matches. Returns list of strings
re.group() # Return one or more groups of the match
re.groups() # Return a tuple with all groups
re.start() # Return start index of group
re.end() # Return end index of group
re.DOTALL # Make . also match newlines
re.IGNORECASE # Case insensitive matching
re.MULTILINE # Multiline matching
re.VERBOSE # Allow verbose regular expressions
re.sub() # Replace any substring in string that matches pattern with the string replacement
re.split() # Split up string using matches as delimiters
# Example
# Parsing Text
data = '''# Measurements started
Sep 9, 9:05, T=22deg
SEP 9, 10:15, T=25deg
# Taking a coffee break
Sep 9, 11:15, T=-10deg
# Weekend
Sept 12, 09:00AM, T=32deg
Oct12 13:00, T=32degr'''

data_lines = data.split('\n')
re.compile('[a-zA-Z]+') # One or more characters between a-z and A-Z
for data_line in data_lines:
    if pattern.search(data_line):
        print(data_line)

# Match beginning of line with one or more characters between a-z and A-Z
# Zero or one time of (one or more characters between 0-9
pattern = re.compile('^[a-zA-Z]+ ?([0-9]+)')
match = pattern.search(data_lines[1])
for data_line in data_lines:
    if match:
        print(data_line)

for data_line in data_lines:
    if data_line[0] == "#":
        continue # Skip lines starting with #
    index = 0
    while data_line[index].isalpha():
        index += 1 # Move ahead on letters
    month_name = data_line[:index] # extract month name
    if data_line[index] == " ":
        index += 1 # Jump passed space
    data_line = data_line[index:] # Remove month name from data_line
    index = 0
    while data_line[index].isdigit():
        index += 1 # Move ahead on letters
    day_number = int(data_line[:index]) # extract day number

