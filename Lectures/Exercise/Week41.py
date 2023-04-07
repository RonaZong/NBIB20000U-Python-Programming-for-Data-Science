import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1
print(np.average(np.random.randint(1, 7, 10000) + np.random.randint(1, 7, 10000)))

# 2
data = np.genfromtxt("experimental_results.txt")
a = np.average(data[:,0])
b = np.average(data[:,1])
print(str(a) + ', ' + str(b))
print(np.average(data, axis=0))
data_subset = data[:500, 1]
data_subset[:] = 0
print(np.average(data, axis=0))

# 3
c = np.random.randint(1, 7, 10000) + np.random.randint(1, 7, 10000)
plt.hist(c,bins=np.arange(1.5, 13.5, 1))
plt.show()

# 4
data = np.genfromtxt("fern_data.txt")
# Edgecolor removes the edges around each point
# Set the size of each point to 0.5
# Set the color of each point to green
plt.scatter(data[:,0],data[:,1],edgecolor='none', s=0.5, color='green') # set opacity
# Remove the axes
plt.axis('off')
plt.show()

# 5
pd_series = pd.Series(range(100))
length = pd_series.astype('string').str.len()
print(length)

# 6
df = pd.read_table('british-english', keep_default_na=False, header=None)
df.columns = ['words']
print(df.loc[df['words'].str.startswith('A')])

# 7
df = pd.read_table('british-english', keep_default_na=False, header=None)
result = df.groupby(df[0].str[0]).count()
print(result)

# 8
result = result.rename_axis(index='letter')
result.columns = ['word count']
result.plot.bar()
