import numpy as np

# read rectangles from input file
rectangles = []
with open('rectangles_y2.txt', 'r') as f:
    for line in f:
        rect = tuple(map(int, line.strip().split(',')))
        rectangles.append(rect)

# create numpy array
arr = np.zeros((1281, 721), dtype=int)

# count rectangles for each point in array
for rect in rectangles:
    x1, y1, x2, y2 = rect
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] += 1

# Export to CSV
np.savetxt("output.csv", arr, delimiter=",", fmt='%i')

# Export to PNG
import matplotlib.pyplot as plt
plt.imshow(arr, cmap='hot', interpolation='nearest')
plt.savefig('output.png')
