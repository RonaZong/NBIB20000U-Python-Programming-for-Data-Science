# Q1
input = open('alice.txt', 'r')
lines = input.readlines()
input.close()

# Q2
number_of_lines = len(lines)
print(number_of_lines)

# Q3
print(lines[41-1])

# Q4
number_of_words = len(lines[43-1].split(' '))
print(number_of_words)

# Q5
junk_file = open('junk.txt', 'w')
junk_file.write(lines[9-1] + lines[10-1] + lines[11 - 1])
junk_file.close()