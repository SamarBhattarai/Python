import numpy as np

array = np.ones((2,2))
print(array)

# Padding a one-dimensional array
array = np.pad(array, pad_width = ((1,0),(0,1)), mode='constant', constant_values = (0,0))
# This array has 2 axes (rows and columns), so the pad_width argument has 2 tuples:
# AxisTupleMeaningAxis 0 (rows)(1, 0)add 1 row of zeros before, 0 rows afterAxis 1 
# (columns)(0, 1)add 0 columns before, 1 column after
print(array)