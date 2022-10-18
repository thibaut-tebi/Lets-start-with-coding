


import pandas as pd

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# make dataframe
arrays = [[0, 0, 1, 1],
          [0, 1, 0, 1]]
data = [1458, 1075, 2884, 2196]
df = pd.DataFrame(data, index=arrays, columns=['frequency'])

# get data from DF series
y1 = df.loc[0,'frequency'].to_list()
y2 = df.loc[1,'frequency'].to_list()

# get data arrays
arr1 = [0] * y1[0] + [1] * y1[1]
arr2 = [0] * y2[0] + [1] * y2[1]

# set matplotlib plot
fig, ax = plt.subplots()

# plot histogram
num_bins = 2
ax.hist([arr1, arr2], num_bins, density=False, label=['bool_loc 0', 'bool_loc 1'])
plt.legend(loc='upper right')
plt.show()
