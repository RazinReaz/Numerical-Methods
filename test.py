import numpy as np

d = np.array([[5, 5, 5, 5], [0, 2, 3, 4]])
d[[0,1],:] = d[[1,0],:]
print(d)
