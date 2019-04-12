"""
Subtractive clustering algorithm :
1) normalize the data using max and min values from all the dimensions
2) calculate potentials.
squash_factor = 1.5
acceptRatio = 0.5
rejectratio = 0.3
rb = radii*squashFactor
alpha = 4 /(radii ** 2)
beta = 4/( rb ** 2)
ndim = no of dimensions --- from dataset=2
npoints = no of points --- from dataset=256*224
radii = radius --- user input 


"""

from matplotlib import pyplot as plt
import numpy as np


# image loading
from PIL import Image

image_matrix = Image.open("lennaJPG.jpg").convert("LA")
x = np.asarray(image_matrix)

# num = int(input("Enter the number of clusters you want : "))
num = 2
"""
x = np.random.rand(10,10)
print(x)
"""

y = x.reshape(1, -1)[0]
y = y.astype(float)


# normalization
max_, min_ = max(y), min(y)
for i in range(len(y)):
    y[i] = (y[i] - min_) / (max_ - min_)

# plot
t = np.linspace(1, len(y), len(y))
plt.scatter(t, y)
plt.show()

# first cluster centre
ra = 0.3
potentials = []
centers = []
potVals = []
temp = 0

for i in range(len(y)):
    p = 0
    for j in range(len(y)):
        euclid_dist = np.dot(y[i] - y[j], y[i] - y[j])
        p = p + np.exp(-(euclid_dist) / (ra / 2) ** 2)
    potentials.append(p)

potVals.append(max(potentials))
array_index = potentials.index(potVals[temp])
m, n = x.shape
centers.append(x[array_index // m, array_index % n])


# next cluster calculations
for _ in range(num - 1):
    rb = 1.5 * ra
    for i in range(len(potentials)):
        p = 0
        for j in range(len(y)):
            euclid_dist_iter = np.dot(y[j] - centers[temp], y[j] - centers[temp])
            potentials[i] = potentials[i] - potVals[temp] * np.exp(
                -(euclid_dist_iter) / (rb / 2) ** 2
            )

    temp += 1
    potVals.append(max([p for p in potentials if p not in potVals]))
    print(potVals)
    array_index_iter = potentials.index(potVals[temp])
    centers.append(x[array_index_iter // m, array_index_iter % n])


print(centers)