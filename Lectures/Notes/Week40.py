# An object has a certain class
# A class corresponds to a template for the creation of objects
# It specifies which attributes an object should have
# This class is used whenever you create a new object

# An object created form a class is called an instance of the class
# An object is said to inherit the attributes of its class

list = [1,2,3,4] # list is an instance of the list class

l = (1,2,3,4) # instance of tuple

a = str(8) # construct string
b = tuple([1,2,3,4]) # construct tuple

class DNA:
    '''Class represents sequences of Deoxyribonucleic acid'''
    def print_nucleotides(self):
        '''Print the possible nucleotide letters to screen'''
        print('ACGT')

    def get_name(self):
        '''Return name attribute'''
        return self.name

    def set_name(self, name):
        '''Set name attribute'''
        self.name = name


dna_object = DNA()
dna_object.print_nucleotides()
dna_object.set_name('E.coli bla')
print(dna_object.get_name())
print(dna_object.name)

# If class B inherits from A
# A is the base-class / super-class of B
# B is a derived-class / sub-class of A
# B is specialization of A
# Inheritance is called is-a relationship

class Person:
    def __init__(self, name, cpr, address):
        self.name = name
        self.cpr = cpr
        self.address = address

class Student(Person):
    def __init__(self, name, cpr, address, courses, grades, enrollment):
        Person.__init__(self, name, cpr, address)
        self.courses = courses
        self.grades = grades
        self.enrollment = enrollment


rona = Student(name='Xingrong Zong', cpr='990524-1234', address='Skovbrynet 2E', courses=['Python', 'Quantum Computing'], grades=['A', 'B'], enrollment='2021' )
albert = Student(name='Albert Einstein', cpr='14031879-1235', address='112 Mercer Street Princeton', courses=['Linear Algebra', 'Relatively'], grades=['B', 'A'], enrollment=1895)

class StudentGroup:
    def __init__(self, students = []):
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def get_names(self):
        names = []
        for student in self.students:
            names.append(student.name)
        return names

team = StudentGroup(students = [rona, albert])
print(team.get_names())

class Staff(Person):
    def __init__(self, name, cpr, address, office, job):
        Person.__init__(self, name, cpr, address)
        self.office = office
        self.job = job

elvis = Staff('Elvis Preslet', '12341234', 'asdfasdf', 12, 'adfalflsdfasdf')

class Researcher(Person):
    def __init__(self, name, cpr, address, office, publications, interests):
        Person.__init__(self, name, cpr, address)
        self.office = office
        self.publications = publications
        self.interests = interests

niels = Researcher(name="Niels Bohr", cpr="07101885-7459", address="Carlsberg Æresbolig, Gamle Carlsbergvej, Valby", office=12, publications=1234, interests="asdfasdf")


# Linear Search
# Binary Search - Exclude half of the list each time
# Dictionary - Hash-function maps key values to indices in a list
# Computational Complexity
# a conservative estimate of the number of steps necessary to complete the algorithm
# expressed in terms of the size of the input n
# formally described using the big-O notation
# Big-O notation: Mathematical notation that describes the asymptotic behaviour of a function
# Think of the time complexity of a program as a function f(n) of the input size n.
# As the input size grows, the execution time typically grows
# The O formalism is designed to give an upper bound


l = [1,2,3,4,5,6,7,8,9,10]
print(l) # Complexity: O(n)

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l) # Complexity: O(n^2 + n) = O(n^2)

# Bubble Sort
l = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l) # Complexity: O(n(n+1)/(2+n)) = O(n^2)

# Built in sort method in python lists is faster.
# Complexity: O(nlog(n))

# What is the complexity of looking up an element in a list using []? O(1)
# What is the complexity of removing an element in a python list using pop()? O(1) at end or O(n) at arbitrary position
# What is the complexity of the strip() method in the string class? O(n), strings are immutable
# What is the complexity of handin4_test.py? O(n), where n is the number of lines in the file

# Exceptions are used to indicate that something exceptional has happened in a program
# Raising an exceptions immediately interrupt the program's execution
# Exceptions are mainly used for:
# Errors and error recovery
# Notifications of special events

# try-catch statements
d = {"Mon":"Monday", "Tue":"Tuesday"};
try:
    d["Wed"]
except:
    print("Key not found in dictionary. Available keys:", d.keys())

# Catch specify exceptions
d = {"Mon": "Monday", "Tue": "Tuesday"};
try:
    d["Wed"]
except KeyError: # Only catch KeyError exceptions
    print("Key not found in dictionary. Available keys:", d.keys())

# try-catch statements
d = {"Mon":"Monday", "Tue":"Tuesday"};
try:
    d["Wed"]
except Exception: # Exception covers both NameError and KeyError
    print("Key not found in dictionary. Available keys:", d.keys())

# Access exception object to gain extra information regarding the error
d = {"Mon":"Monday", "Tue":"Tuesday"};
try:
    d["Wed"]
except Exception as error: # save error object
    # error contains information about key that failed
    print("Information about error:" + str(error))

# Raise built-in exceptions
raise KeyError

# Assert statement
if not condition:
    raise exception
# Raise an AssertionError if condition is not True
assert contition

# Define exceptions
class MyException(Exception):
    pass
raise MyException

# try-except-finally
try:
    data = open("british-english")
    words = {}
    for i, line in enumerate(data):
        words[line.strip()] = i
    print(words["bokeh"])
except KeyError as error:
    print("Word %s not found" % str(error))
finally:
    data.close()

# with statement
thing = initialize_thing()
try:
    pass
finally:
    finnalize_thing()
# Shortcut
with initialize_thing() as thing:
    pass

with open("british-english") as data:
    words = {}
    for i, line in enumerate(data):
        words[line.strip()] = i
    print(words["bokeh"])