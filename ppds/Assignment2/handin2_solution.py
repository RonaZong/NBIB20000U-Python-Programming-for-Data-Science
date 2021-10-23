row_list = [[0.1, 0.2], [0.4, 0.6], [0.7, 0.9]]
row1 = []
row2 = []
for i in row_list:
    row1.append(row_list[0])
    row2.append(row_list[1])

print(row1, row2)


column_list = [[0.1, 0.4, 0.7], [0.2, 0.6, 0.9]]
column1 = sum(column_list[0]) / len(column_list[0])
print(column1)