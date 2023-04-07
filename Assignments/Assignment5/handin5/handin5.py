def wordfile_to_list(filename):
    '''Test wordfile_to_list function'''
    input = open(filename)
    data = input.readlines()
    list = []
    for line in data:
        line = line.strip()
        print(type(line))
        list.append(line)
    return list

def wordfile_differences_linear_search(filename1, filename2):
    '''Test wordfile_differences_linear_search function'''
    list1 = wordfile_to_list(filename1)
    list2 = wordfile_to_list(filename2)
    list_differences = []
    for i in list1:
        if i not in list2:
            list_differences.append(i)
    return list_differences

def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False

def wordfile_differences_binary_search(filename1, filename2):
    '''Test wordfile_differences_binary_search function'''
    list1 = wordfile_to_list(filename1)
    list2 = wordfile_to_list(filename2)
    list2 = sorted(list2)
    list_differences = []
    for i in list1:
        if binary_search(list2, i) == False:
            list_differences.append(i)
    return list_differences

def wordfile_to_dict(filename):
    '''Test the wordfile_to_dict function'''
    list = wordfile_to_list(filename)
    dictionary = []
    for i in list:
        dictionary.append([i, 0])
    dictionary = dict(dictionary)
    return dictionary

def wordfile_differences_dict_search(filename1, filename2):
    '''Test the wordfile_differences_dict_search function'''
    list1 = wordfile_to_list(filename1)
    dict2 = wordfile_to_dict(filename2)
    list_differences = []
    for i in list1:
        if i not in dict2.keys():
            list_differences.append(i)
    return list_differences