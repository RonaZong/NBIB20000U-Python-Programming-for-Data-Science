import exam
import matplotlib.pyplot as plt

# Q1
# 1
exam.clean_si_table_data("fig_s14_data.txt", "fig_s14_data_cleaned.txt")
# 2
si_table_data = exam.parse_si_table_data("fig_s14_data_cleaned.txt")
print(si_table_data['Current (~2010) Diet']['Land Use (million ha)'])

# Q2
# 1
si_table_data_grouped = exam.parse_si_table_data_grouped("fig_s14_data_cleaned.txt")
print(si_table_data_grouped['Current (~2010) Diet']['Land Use (million ha)']['Arable Land'])
# 2
fig, ax = plt.subplots()
exam.create_bar_plot(ax, si_table_data_grouped['Current (~2010) Diet']['Food Miles (million tkm, farm to consumer)'])
plt.savefig('air_share.png')
# 3
fig, ax = plt.subplots()
exam.create_stacked_bar_plot(ax, si_table_data_grouped, 'GHG Emiss. (Gt CO2eq)')
plt.savefig('scenarios.png')

# Q3
# 1
data = exam.read_excel_data("LCA+Meta-Analysis+of+Food+Products+-+Full+Model+v0+(1).xlsx", "Database", 2)
# 2
emission_means = exam.extract_emission_means(data)
print(emission_means)
# 3

# Q4
# Extract columns of interest, and remove any rows containing missing values
data_subset = data[['GHG Emis \n(kg CO2 eq)', 'Tran & Str', 'Product']].dropna()

# Convert Pandas dataframe to a dictionary of dictionaries
data_dict = {'emission': data_subset['GHG Emis \n(kg CO2 eq)'].to_dict(),
             'transport': data_subset['Tran & Str'].to_dict(),
	     'product': data_subset['Product'].to_dict()}