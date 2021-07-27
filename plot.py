import matplotlib.pyplot as plt
import numpy as np
import sys

arr = np.genfromtxt(sys.argv[1:][0], delimiter=',')

arr_T = arr.T

plt.scatter(arr_T[4], arr_T[2], c=0-arr_T[4], cmap='RdYlBu', s=30,  edgecolors='black')
plt.clim(-2,2) 
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('V magnitude')
plt.show()
