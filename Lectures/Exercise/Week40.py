# 1
class MyInfo():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print(self):
        print('Name: ' + self.firstname + ' ' + self.lastname + '\nAge: ' + str(self.age))

info = MyInfo("Xingrong", "Zong", 22)
info.print()

# 2
try:
    print(I_love_python)
except Exception as error: # NameError
    print("Information about error:" + str(error))

l = [1,2,3,4]
try:
    print(l[4])
except Exception as error: # IndexError
    print("Information about error:" + str(error))

try:
    print(1/0)
except Exception as error: # ZeroDivisionError
    print("Information about error:" + str(error))

# 3
x = 2
try:
    assert x > 0 and x < 10
    assert x < 0 and x > 10
except Exception as error: # AssertionError
    print("Assertion failed" + str(error))

def evenNumber(value):
    assert value % 2 == 0
try:
    evenNumber(5) # AssertionError
except Exception as error:
    print("Assertion failed" + str(error))

# 4
# open and close the file
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

# open and close the file
with open("british-english") as data:
    words = {}
    for i, line in enumerate(data):
        words[line.strip()] = i
    print(words["bokeh"])