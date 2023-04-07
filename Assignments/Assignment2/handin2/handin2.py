#Q1
def read_data(filename):
    '''Check read_data function'''
    input = open(filename, 'r')
    data = input.read().splitlines()
    newData = []
    for line in data:
        line = line.split()
        newData.append([float(line[0]), float(line[1])])
    return newData
list_of_rows = read_data('experimental_results.txt')
print(list_of_rows)
print(len(list_of_rows))
print(len(list_of_rows[-1]))

#Q2
def calc_averages(list):
    '''Check calc_averages function'''
    col1 = 0
    col2 = 0
    for tup in list:
        col1 += tup[0]
        col2 += tup[1]
    return col1 / len(list), col2 / len(list)
col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)

#Q3
def transpose_data(list):
    '''Check transpose_data function'''
    list1 = []
    list2 = []
    for tup in list:
        list1.append(tup[0])
        list2.append(tup[1])
    return list1, list2
list_of_columns = transpose_data(list_of_rows)
print(list_of_columns)
print(len(list_of_columns))
print(len(list_of_columns[-1]))

# sum of column list for Q2
print(sum(list_of_columns[0])/len(list_of_columns[0]))
print(sum(list_of_columns[1])/len(list_of_columns[1]))

