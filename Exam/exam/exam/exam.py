import re
import matplotlib.axes
import pandas as pd
import openpyxl

# Q1. Does buying local matter?
def clean_si_table_data(input_filename, output_filename):
    '''1. Remove speech bubble inserts and write the cleaned result to a new file'''
    input = open(input_filename, "r")
    data = input.read()
    speech_bubble1 = "\[ Stimulants 17%\nSugar Cane 17%\nPalm 7%\nCereals 12%\nCassava 10%\nSoy 33% \]"
    new_data = re.sub(speech_bubble1, "", data)
    speech_bubble2 = "\[ Reduction in food\nwaste and food\nmiles associated\nwith changing\nfrom animal to\nvegetable proteins\nis offset by higher\nconsumption of\nfresh fruit and\nvegetables \]"
    new_data = re.sub(speech_bubble2, "", new_data)
    output = open(output_filename, "w")
    output.write(new_data)
    input.close()
    output.close()

def parse_si_table_data(filename):
    '''2. Return a dictionary of dictionaries, outer corresponds to column labels, inner corresponds to row labels'''
    # input = open(filename)
    # data = input.readlines()
    # dictionary = {}
    # column_labels = data[0].split(";")
    # row_labels = []
    # values = []
    # for line in data[2:]:
    #     line = line.split(";")
    #     row_labels.append(line[0])
    #     for value in line[1:]:
    #         value = value.strip()
    #         values.append(value)
    # for c_l in column_labels[1:]:
    #     c_l = c_l.strip()
    #     dictionary[c_l] = {}
    # index = 0
    # for r_l in row_labels:
    #     r_l = r_l.strip()
    #     for c_l in column_labels[1:]:
    #         c_l = c_l.strip()
    #         dictionary[c_l][r_l] = values[index]
    #         if index + 1 >= len(values):
    #             break
    #         else:
    #             index += 1
    input = open(filename)
    data = input.readlines()
    dictionary = {}
    column_labels = []
    for c_l in data[0].split(";")[1:]:
        c_l = c_l.strip()
        column_labels.append(c_l)
        dictionary[c_l] = {}
    rows = []
    for line in data[2:]:
        line = line.split(";")
        if line == ["\n"]:
            continue
        else:
            rows.append(line)
    j = 1  # index for row
    for c_l in column_labels:
        for row in rows:
            r_l = row[0].strip()
            dictionary[c_l][r_l] = row[j].strip()
        j += 1
    input.close()
    return dictionary

# Q2. Restructing into groups and plotting
def parse_si_table_data_grouped(filename):
    '''1. Return a dictionary of dictionaries of dictionaries, outer corresponds to column labels, middle corresponds to grouped row labels, inner corresponds to singled row labels'''
    input = open(filename)
    data = input.readlines()
    dictionary = {}
    column_labels = []
    for c_l in data[0].split(";")[1:]:
        c_l = c_l.strip()
        column_labels.append(c_l)
        dictionary[c_l] = {}
    rows = []
    for line in data[1:]:
        line = line.split(";")
        rows.append(line)
    k = 1  # index for row
    r_l_p = ""
    for c_l in column_labels:
        j = 0  # index for rows
        for row in rows:
            r_l = row[0].strip()
            if row == ["\n"]:
                j += 1
                continue
            if rows[j - 1] == ["\n"]:
                r_l_p = rows[j][0].strip()
                dictionary[c_l][r_l_p] = {}
                j += 1
                continue
            else:
                dictionary[c_l][r_l_p][r_l] = row[k].strip()
                j += 1
        k += 1
    input.close()
    return dictionary

def create_bar_plot(ax, dictionary):
    '''2. Create a bar plot'''
    labels = []
    for label in dictionary.keys():
        labels.append(label)
    values = []
    for value in dictionary.values():
        value = float(value.replace(",", ""))
        values.append(value)
    ax.bar(x=labels, height=values, width=0.3)

def generate_stack(dictionary):
    '''3. Create a stacked bar plot'''
    labels = []
    for label in dictionary.keys():
        labels.append(label)
    values = []
    for value in dictionary.values():
        value = float(value.replace(",", ""))
        values.append(value)
    offsets = []
    offset = 0
    for i in range(len(values)):
        if i == 0:
            offsets.append((0, offset + values[i]))
        else:
            offsets.append((offset, offset + values[i]))
        offset += values[i]
    return offsets, labels

def create_stacked_bar_plot(ax, grouped_data_dictionary, selected_group_name):
    '''Helper function for creating stacked bar plot'''

    # This helper function uses numpy. Importing it here for convenience.
    import numpy as np

    all_offsets = []
    all_labels = []

    # Iterate over scenarios, and use user-defined generate_stack function
    for scenario in grouped_data_dictionary:
        group_dict = grouped_data_dictionary[scenario][selected_group_name]
        offsets, labels = generate_stack(group_dict)

        all_offsets.append(offsets)
        all_labels.append(labels)

    # Convert to numpy array
    all_offsets = np.array(all_offsets)
    all_labels = np.array(all_labels)

    # Check that labels reported in different iterations are the same
    assert np.unique(all_labels, axis=0).shape[0] == 1

    # Extract labels that will be on the x-axis
    scenario_labels = list(grouped_data_dictionary.keys())

    # Iterate over the members of the group
    for j in range(all_offsets.shape[1]):
        ax.axes.bar(scenario_labels,
               all_offsets[:, j, 1] - all_offsets[:, j, 0],
               label=all_labels[0, j],
               bottom=all_offsets[:, j, 0])

    ax.legend()
    ax.set_ylabel(selected_group_name)
    ax.tick_params(axis='x', labelrotation=10)


# Q3. Climate impact of different foods
def read_excel_data(filename, sheetname, linenumber):
    '''1. Read excel sheet into a pandas dataframe'''
    # data = pd.read_excel(data=filename,
    #                      sheet_name=sheetname, # Data from sheet "Database"
    #                      index_col=0, # The fist column contains the index labels
    #                      header = linenumber,  # Take column names from 3rd row
    #                      )
    input = openpyxl.load_workbook(filename)
    sheet = input[sheetname]
    data = sheet.values
    df = pd.DataFrame(data)
    df.columns = df.iloc[linenumber] # Get the 3rd line in file as a header
    df = df.iloc[5:].reset_index(drop=True)
    # size = 488
    # df.drop(columns=df.columns[487], axis=1, inplace=True)
    return df

# import json
# import gzip
# import pandas as pd
# with gzip.open("data.json.gz", "rb") as f:
#     a = pd.read_json(json.loads(f.read().decode("ascii")))
#     print(a)

def extract_emission_means(dataframe):
    '''2. Return a pandas series'''
    # ID_LOSS = index, emissions = values
    ID_LOSS_grps = dataframe.groupby("ID_LOSS")
    food_type = ID_LOSS_grps.groups
    name = food_type.keys()
    number = food_type.values()
    emission_grps = dataframe.groupby("GHG Emis \n(kg CO2 eq)")
    emission = emission_grps.groups
    value = emission.values()
    means = value / number
    pd_series = pd.Series(data=means, index=name)
    print(pd_series)
    return pd_series

# data = read_excel_data("LCA+Meta-Analysis+of+Food+Products+-+Full+Model+v0+(1).xlsx", "Database", 2)
# emission_means = extract_emission_means(data)
# print(emission_means)

def extract_emission_means_stddevs():
    '''3. Return a dataframe with mean and standard deviation'''
    data = pd.DataFrame(columns=['mean', 'stddev'])
    return data

# Q4. For which food products does transportation matter?
