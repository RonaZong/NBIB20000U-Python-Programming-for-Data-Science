print("Hello, World!")

# Square of the average of all prime numbers between 0 and 10
square = ((2+3+5+7)/4.0)**2
print(square)

a = 2
print(a)
print(a * 2)

a = "hello"
print(a)

drink_limit = 4
print(7/2) #python2: integer division
print(7/2.)
print(7/float(2))

x = 3
y = 4
print(x<y)
print(x>y)
print(x==y)

x = 1
print((x > 0) and (x < 10))
print((x > 0) or (x < 10))
print((x > 0) and (x > 10))
print((x > 0) or (x > 10))

str1 = """Hello, World!"""
print(str1)

# True
print("a" < "hello")
print("ux" in "Linux")

# \n new line; \t tab; \' single quote; \" double quote; \\ backslash
print("1\t2\n3")
print("\"Hello\"")
print("\\Hello\\")

number_of_apples = 6
print("I have " + str(number_of_apples) + " apples")

s = "hello"
print(s[0])
print(s[4])
print(s[-1])

# Exercises
# 4 + 3 = 7
print(4+6 / 2)
# 10 / 2 = 5
print((4 + 6) / 2)

# x = 1
x=4; x+=1; x-=2; x*=3; x//=2; x**=2; x%=5
print(x)

# True
print(not(not(x>0) or not (x < 10)))
print(not (x<=0) or (x>=10))
print((x > 0) and (x < 10))

firstname = "Xingrong"
lastname = "Zong"
age = 22
print("Name: " + firstname + " " + lastname + "\nAge: " + str(age))
age = str(22)
print("Name: " + firstname + " " + lastname + "\nAge: " + age)

country_name = "Denmark"
continent_name = "Europe"
populatiom = str(5600000)
print("Country: " + country_name + "\nContinent: " + continent_name + "\nPopulation: " + populatiom)