import re

def read_fasta(filename):
    '''Test read_fasta function'''
    input = open(filename, 'r')
    data = input.readlines()
    dictionary = []
    key = []
    sequence = []
    sequence_data = ''
    i = 0
    for line in data:
        if re.match('>\w+', line):
            key_data = re.findall('>\w+', line)
            key_data = re.search('\w+', str(key_data))
            key.append(key_data.group())
            if i < len(data):
                i += 1
        else:
            sequence_data += line.strip('\n')
            if i < len(data):
                if i + 1 == len(data):
                    sequence.append(sequence_data)
                    sequence_data = ''
                elif re.findall('>\w+', data[i+1]):
                    sequence.append(sequence_data)
                    sequence_data = ''
                i += 1
    for k in range(len(key)):
        dictionary.append([key[k], sequence[k]])
    dictionary = dict(dictionary)
    return dictionary

def find_prot(dictionary, protein_name):
    '''Test find_prot function'''
    for k, v in dictionary.items():
        if re.search(protein_name, k):
            return v
        else:
            continue
    # for i in range(len(dictionary)):
    #     if re.search(protein_name, str(dictionary.keys())):
    #         sequence = dictionary[protein_name]
    #         return sequence
    #     else:
    #         continue
    print('Error: protein name ' + protein_name + ' not found')
    return None

def find_prot2(dictionary, regular_expression):
    '''Test find_prot2 function'''
    keys_list = []
    for k, v in dictionary.items():
        if re.search(regular_expression, k):
            keys_list.append(k)
        else:
            continue
    # for i in range(len(dictionary)):
    #     if re.search(regular_expression, str(dictionary.keys())):
    #         keys_list.append(dictionary.k)
    #     else:
    #         continue
    return keys_list