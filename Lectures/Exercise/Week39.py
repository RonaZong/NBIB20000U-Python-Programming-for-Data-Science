#1
def randint():
    print("hello")
randint()

import random as rnd
print(rnd.randint(1, 6))

from random import randint as rnd_randint
print(rnd_randint(1, 6))

#2
# Import regular expressions
import re
pattern1 = re.compile('[a-zA-Z]+') # RE: one or more characters between a-z and A-Z
pattern1 = re.compile('[0-9]+') # One or more characters between 0-9
print(pattern1.match('13')) # Pattern matched
print(pattern1.match('hello')) # Pattern not matched

# 5
data = '''# Measurements started
Sep 9, 9:05, T=22deg
SEP 9, 10:15, T=25deg
# Taking a coffee break
Sep 9, 11:15, T=-10deg
# Weekend
Sept 12, 09:00AM, T=32deg
Oct12 13:00, T=32degr'''

data_lines = data.split('\n')
pattern2 = re.compile('[0-9]+') # One or more characters between 0-9

for data_line in data_lines:
    # Find lines that contains one or more 0-9
    if pattern2.search(data_line):
        print(data_line)

pattern3 = re.compile('^[a-zA-Z]+ ?([0-9]+)')
match = pattern3.search(data_lines[1])
# Find a match with 'a-z'+'a-z'+...+space+'0-9'
if match:
    print(match.groups()) # All specified groups
    print(match.group()) # Group 0 -> entire matching str
    print(match.group(1)) # Group 1 -> first set of ()

# 6
for data_line in data_lines:
    if re.search('T=[0-9]+', data_line):
        temp = re.findall('T=[0-9]+', data_line)
        value = re.search('[0-9]+', str(temp))
        print(value.group())


# 7
text1 = 'Barack Obama'
pattern4 = re.compile('([A-Za-z]+).*([A-Za-z]+)')
print(pattern4.match(text1).groups())

pattern4 = re.compile('([A-Za-z]+).*?([A-Za-z]+)')
print(pattern4.match(text1).groups())

pattern4 = re.compile('([A-Za-z]+)\s*([A-Za-z]+)')
print(pattern4.match(text1).groups())

# 8
pattern5 = re.compile('\d+\\b')
print(pattern5.match('22 '))
print(pattern5.match('22a '))

pattern5 = re.compile(r'\d+\b')
print(pattern5.match('22 '))
print(pattern5.match('22a '))

# 9
text2 = 'linux\npython'
pattern6 = re.compile('.*')
pattern7 = re.compile('.*', re.DOTALL)
print(pattern6.findall(text2))
print(pattern7.findall(text2))

# 10
text3 = 'one|two@three$four'
pattern8 = re.compile('[|@$]')
print(pattern8.split(text3))
print(pattern8.sub(' - ', text3))

# 11
text4 = 'Hello bla bla bla hello.'
pattern9 = re.compile('([Hh])ello')
print(pattern9.sub(r'\1ey', text4))
