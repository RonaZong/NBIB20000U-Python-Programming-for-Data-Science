def unscramble_attempt1(list):
    '''Check for unscramble_attempt1 function'''
    return sorted(list)
scrambled_file = open("m_scrambled.txt", 'r')
unscrambled_lines = unscramble_attempt1(scrambled_file.readlines())
print("".join(unscrambled_lines))
scrambled_file.close()

def unscramble_attempt2(list):
    '''Check for unscramble_attempt2 function'''
    newData = []
    for line in list:
        line = line.split(" ", 1)
        newData.append([int(line[0]), line[1]])
    newData = sorted(newData)
    # print(type(newData[0]))
    new_string_list = []
    for line in newData:
        new_string_list.append(str(line[0]) + " " + line[1])
    # print(type(new_string_list[1]))
    # print(newData)
    # for line in list:
    #     line = tuple(line)
    #     string = []
    #     for i in range(3, len(line)):
    #         string.append(line[i])
    #     newData.append([line[0] + line[1] + line[2], string])
    # print(newData[0])
    return new_string_list
def take_first(list):
    return int(list[0])
scrambled_file = open("m_scrambled.txt")
unscrambled_lines = unscramble_attempt2(scrambled_file.readlines())
print("".join(unscrambled_lines))
scrambled_file.close()