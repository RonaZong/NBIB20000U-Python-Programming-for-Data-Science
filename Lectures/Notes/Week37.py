print("Name: {}\nAge: {} ".format("Xingrong Zong", 22))
print("Name: {firstname} {lastname}\nAge: {age:d}".format(firstname = "Xingrong", lastname = "Zong", age = 22))
print("Name: %(firstname)s %(lastname)s\nAge: %(age)d" % {"firstname": "Xingrong", "lastname": "Zong", "age": 22})


# 0 1 2 3 4, each line
print(("%s\n"*5)%tuple(range(5)))
print("%s\n%s\n%s\n%s\n%s\n"%(0,1,2,3,4))

# the amount on both sides has to be the same
# print(("%s\n"*4)%tuple(range(5)))

import random
# [0.0, 1.0)
x = random.random()
if 0 <= x < 1.0 / 6:
    print(1)
elif 1.0 / 6 <= x < 2.0 / 6:
    print(2)
elif 2.0 / 6 <= x < 3.0 / 6:
    print(3)
elif 3.0 / 6 <= x < 4.0 / 6:
    print(4)
elif 4.0 / 6 <= x < 5.0 / 6:
    print(5)
else:
    print(6)

print(int(x * 6 + 1))

height = random.randrange(40, 190)
if height >= 120:
    print("Welcome")
    if height < 130:
        print("You have to go with an adult")
    else:
        print("You can get on the ride")
else:
    print("Sorry, you could not get on this machine")

if height >= 130:
    print("Welcome")
elif 120 <= height < 130:
        print("You have to go with an adult")
else:
    print("Sorry, you could not get on this machine")

i = 3
while (i > 0):
    print(i)
    i -= 1

k = 1
while (k <= 10):
    if k % 3 != 0:
        print(k)
    k += 1

for h in range(11):
    if h % 3 != 0:
        print(h)

for i in range(3):
    print(i)

container = ["a", "b", "c"]
for val in container:
    print(val)
for i in range(len(container)):
    print(container[i])
for i, val in enumerate(container):
    print(val)
print(list(enumerate(container)))

c = [(0,0,1), [0,2,1], [5,2,4], [3,6,4]]
for tup in c:
    print(tup)
    for entry in tup:
        print(entry)

presidents = [{'Name': 'Barack Obama', 'Age': 56},
              {'Name': 'Bill Clinton', 'Age': 71}]
for dictionary in presidents:
    print(dictionary)
    for key in dictionary.keys():
        print("%s: %s" % (dictionary[key], key))


container = [6, 9, 4, 8, 7, 1, 2]
i = 0
while (i < len(container)):
    print(container[i])
    i += 1

for val in container:
    print(val)


for i in range(1, len(container)): # i = 1~7
    if container[i] > container[i - 1]:
        print(container[i])

for i, entry in enumerate(container):
    if i > 0 and entry > container[i - 1]:
        print(entry)