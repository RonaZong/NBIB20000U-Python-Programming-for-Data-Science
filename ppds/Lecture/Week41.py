# Python Package Index (PyPI)
# grmaster: Module for dividing students into groups
# sudokumaker: Create sudoku puzzles
# IMDb: Query the internet movie database
# Pandas: Python module for data manipulation similar to what can do in R(i.e. arrays with labels)
# Scikit-learn: A data mining and machine learning toolkit: classification, clustering, regression, etc
# Tensorflow/Pytorch: Machine learning libraries - with particular focus on neural networks and deep learning
# Numpy: Vector and matrix operations
# Matplotlib: Visualization
# Scipy: Numerical integration, optimization, special functions
# Biopython: Various tools for bioinformatics and computational biology
# Sequence class for manipulation biological sequences
# Parsing and iterating over various formats: fasta, blast, genbank, pubmed, etc
# Interfaces to external programs: multiple sequence alignment, blast
# Tools for structural biology: PDB
# Phylogenetic tools

# Python package managers
# easy_install
# pip
# Install external modules
# pip install package-name
# pip install --user package-name
# Uninstall packages
# pip uninstall package-name
# anaconda
# Can install non-python dependencies if necessary
# Makes it easy to create different environments, containing different versions of modules (and different versions of python)
# Has a more sophisticated dependency resolution method
# conda install some-package-name

# Numpy
# Make it easy to perform operations on a collection of numbers
# Make it easy to work with tables (matrices) of numbers
# Much faster than writing loops in python
import numpy as np
# contain elements of the same type
# if not specified, numpy will take a guess
a = np.array([1,2,3,4], np.float_) # list, np.int, np.bool
b = np.array((1,2,3,4)) # tuple
# Range of numbers, 2, 2.1, 2.2, 2.3
c = np.arange(2.0, 2.4, 0.1)
print(c)
print(c[1]) # index 1
# Zeros
d = np.zeros(4)
print(d)
# Ones
e = np.ones(4)
print(e)
f = np.arange(1,4)
print(f+f)
print(f*f)
print(f/f)
print(np.cos(f))
# Random floating point numbers between 0 and 1
g = np.random.rand(3)
print(g)
# Random integers
h = np.random.randint(1,3,5)
print(h) # 5 numbers between 1 and 3, 3 not included
# Different distributions
i = np.random.standard_normal(2)
print(i) # normal distr: mean = 0, stddev = 1
# Multidimensional arrays
j = np.array([[1,2,3,4], [5,6,7,8]])
print(j)
print(j[0,2]) # row index 0, column index 2
print(j[0,1:3]) # row index 0, column index 1 and 2
print(j[0:2,1]) # row index 0 and 1, column index 1
print(j[:,1]) # all column index 1
j[:,3] = 0 # assignment
print(j)
j = np.array([[1,2,3,4], [5,6,7,8]])
print(j < 4) # boolean arrays
mask = j < 4 # boolean array
print(j[mask]) # Use mask as index
# 3 values in one dimension
k = np.arange(1,4)
print(k)
print(k.shape) # specify number of values in each dimension
# 2 rows and 4 columns
l = np.array([[1,2,3,4], [5,6,7,8]])
print(l)
print(l.shape)
# Initializing
m = np.zeros(shape=(2,3))
print(m)
n = np.random.random((2,3))
print(n)
# Initializing from file
o = np.genfromtxt("british-english")
print(o)
# Slices are references
p = np.array([[1,2,3], [4,5,6], [7,8,9]])
q = p[0:2, 0:2]
print(q)
q[0,0] = 8
print(q)
print(p)
# Large data sets
q = np.copy(p[0:2,0:2])

# Matplotlib
import matplotlib.pyplot as plt
r = np.arange(0,10,0.1)
s = np.cos(r)
t = np.sin(r)
plt.plot(r,s,label='cosine')
plt.plot(r,t,label='sine')
plt.legend()
plt.show()
# plt.savefig('plot.png', transparent=True)
# Histograms
u = np.random.standard_normal(10000)
plt.hist(u,bins=100)
plt.show()
# Scatter Plot
# 2D-Gauss distribution
v = np.random.multivariate_normal(
    mean=(1,2),
    cov=[[1,-0.5],[-0.5,1]],
    size=1000
)
plt.scatter(v[:,0],v[:,1])
plt.show()
# Box Plot
# Two different distributions
w = [np.random.normal(0,1,1000), np.random.normal(1,0.5,1000)]
plt.boxplot(w)
plt.show()
# Violin Plot
# Two different distributions
x = [np.random.normal(0,1,10000), np.random.normal(1,0.5,10000)]
plt.violinplot(x)
plt.show()
# Opacity
# Create distribution of points
y = np.random.random((50,2))
# What does this line do?
z = np.random.randint(10,1000,y.shape[0])
# Create scatter plot
plt.scatter(y[:,0],y[:,1],s=z,alpha=0.5) # set opacity
plt.show()

# Pandas
# A library for data manipulation and analysis
# Easy to work with structured tables of numbers
# Main difference from Numpy: data is labeled
# Two data types
# Series: like a 1D numpy array, but with labels
# Behave as arrays and dicts
# Dataframe: a 2D data structure with labeled columns
import pandas as pd
np_array = np.array([1.0,2.0,3.0])
# Convert numpy array to pandas series
pd_series = pd.Series(np_array, index=['a','b','c'])
print(pd_series)
# Conver dictionary to pandas series
dictionary = {'a':1.0,'b':2.0,'c':3.0}
pd_series = pd.Series(dictionary)
print(pd_series)
# Labels are used for alignment
print(pd_series + pd_series[1:])
print((pd_series + pd_series[1:]).dropna()) # Explicitly drop
pd_series = pd.Series({'a':'I','b':'love','c':'python'})
print(pd_series.str.upper())
# Categorical
series = pd.Series(['male', 'female', 'female'],dtype='category')
series = pd.Series(['male', 'female', 'female']).astype('category')
series = pd.Series(pd.Categorical(['male', 'female', 'female']))
series = pd.Series(pd.Categorical(['male', 'female', 'female'], categories=['female', 'male']))
print(series.cat.categories)
# Dataframe
# Equivalent to a SAS dataset, an R data frame or an SQL table
# Can be thought of as a dict of Series
# index: row labels
# columns: column labels
np_array = np.arange(6).reshape((2,3))
df = pd.DataFrame(np_array, index=['a','b'], columns=['col1','col2','col3'])
print(df)
print(df.index)
print(df.columns)
print(df.values)
# from dictrionary of lists
dict_of_lists = {'col1':[0,3],'col2':[1,4],'col3':[2,5]}
df = pd.DataFrame(dict_of_lists,index=['a','b'])
print(df)
# if index is not specified, it will use [0,1,...]
# from list of dictionaries
list_of_dicts = [{'col1':0,'col2':1,'col3':2},
                 {'col1':3,'col2':4,'col3':5}]
df = pd.DataFrame(list_of_dicts,index=['a','b'])
print(df)
# Index into a dataframe
# General - also supports slicing
# Get by label: df.loc[row_label, col_label]
# Get by index: df.iloc[row_index, col_index]
# Faster - for lookup of single values
# Get by label: df.at[row_label, col_label]
# Get by index: df.iat[row_index, col_index]
print(df.loc['a', :'col2'])
print(df.loc[:, 'col3'] > 2)
# Add columns
np_array = np.arange(6).reshape((3,2))
df = pd.DataFrame(np_array,index=['a','b','c'],columns=['col1','col2'])
df.loc[:,'col3'] = df.loc[:,'col1'] # add 'col3' - copy
df.assign(col4 = df.loc[:,'col1'])
df.insert(0,'col0',df.loc[:,'col1']) # insert at a specific location
print(df)
# Add rows
np_array = np.arange(6).reshape((3,2))
df = pd.DataFrame(np_array,index=['a','b','c'],columns=['col1','col2'])
df.loc['d',:] = df.loc['a',:] # Add 'd'
df.append(df.loc['a',:])
print(df)
# Descriptive statistics
# Long list of standard operations: .mean(), .std(), .var(), .min(), .max(), .sumsum(), .sumprod()
np_array = np.arange(9).reshape((3,3))
df1 = pd.DataFrame(np_array)
df2 = pd.DataFrame(np_array[:2,:2])
print((df1+df2).sum(axis=0))
print((df1+df2).isna()) # detect missing values
print((df1+df2).fillna(0.0)) # replace missing values
# drop missing values: .dropna()
# replace missing: .interpolate()
# Sorting labels
print(df.sort_index(axis=1,ascending=False))
# Sorting values
print(df.sort_values(by='col2',ascending=False))
# Concatenating
print(pd.concat([df1,df2],axis=1))
# Merging
df1 = pd.DataFrame({'id':[1,2,3],'gender':pd.Categorical(['male','female','female'])})
df2 = pd.DataFrame({'id':[1,2,3],'name':pd.Categorical(['Bob','Alice','Anna'])})
pd.merge(df1,df2,on='id')
df1 = pd.DataFrame({'gender':pd.Categorical(['male','female','female'])})
df2 = pd.DataFrame({'name':pd.Categorical(['Bob','Alice','Anna'])})
pd.merge(df1,df2,left_index=True,right_index=True)
# Grouping
df = pd.DataFrame({'name':pd.Categorical(['Bob','Alice','Anna']),
                   'gender':pd.Categorical(['male','female','female']),
                   'height':[170,180,165]})
gender_grps = df.groupby('gender')
print(gender_grps)
df.groupby(df['name'].str.len()) # dynamically created series
print(gender_grps.groups)
for name,grp in gender_grps:
    print(name)
    print(grp)
print(gender_grps.agg({'height':np.average}))
# Working with time data
idx = pd.date_range('21/10/2021 08:00',periods=3,freq='H')
series = pd.Series(np.arange(len(idx)),index=idx)
print(series)
print(series.asfreq('30Min')) # Change frequency
print(series.asfreq('30Min').interpolate()) # Specify new values
# Plotting
df = pd.DataFrame(np.arange(14).reshape([7,2]), columns=['first','second'],index=idx)
df.plot()