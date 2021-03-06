
#importing modules
import nibabel as nib
from tkinter.filedialog import askopenfilename
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# interactively ask for the .nii.gz file
filename = askopenfilename(title="Open File")
print(filename)

image = nib.load(filename)       #from nibabel.testing import data_path
image_data = image.get_data()

ra = 0.3
rb = ra * 1.5
Eup = 0.5
Edown = 0.15
colors_options = 'rgb'
cluster_center = []

"""
def set_colors(labels, colors=colors_options):
    colored_labels = []
    for label in labels:
        colored_labels.append(colors[label])
    return colored_labels
"""
for k in range(120,161,4):
    DataMatrix = image_data[:,:,k]
    print("Image",k)
    # normalization
    y = DataMatrix.reshape(1,-1)[0]
    y = y.astype(float)
    max_,min_ = max(y),min(y)
    for i in range(len(DataMatrix)):
        for j in range(len(DataMatrix[0])):
            DataMatrix[i][j] = (DataMatrix[i][j] - min_)/(max_ - min_)

    kmeans = KMeans(n_clusters=10).fit(DataMatrix)

    labels = kmeans.labels_
    print("\nThe Labels in the Clustering are:\n")
    print(labels)
    """
    colors = set_colors(labels)
    """
    centroids = kmeans.cluster_centers_
    print("\nThe Centroids in the Image are:\n")
    for i in range(len(centroids)):
        print("Center c",i+1,": ",centroids[i])
    DataMatrix = []

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(normalized_data_matrix[:, 0], normalized_data_matrix[:, 1], normalized_data_matrix[:, 2], c=colors,
           alpha=0.1)
for idx, centroid in enumerate(centroids):
    ax.scatter(*centroid, c=colors_options[idx], s=150, marker='X', label='Cluster '+str(idx+1))

#plt.title('K-means Clusters')
# plt.show()

print('Summary of the data set')
print(DataFrame.describe(), '\n')

print('K-means cluster centers')
print('c1 = {} \nc2 = {} \nc3 = {}\n'.format(kmeans.cluster_centers_[0],
                                         kmeans.cluster_centers_[1],
                                         kmeans.cluster_centers_[2]))

# initialize potentials
size = len(normalized_data_matrix)
potential = [0.0] * size
for i in range(size):
    Xi = normalized_data_matrix[i]
    for j in range(i + 1, size):
        Xj = normalized_data_matrix[j]
        value = np.exp(-4.0 * ((Xi[0] - Xj[0]) ** 2 + (Xi[1] - Xj[1]) ** 2 + (Xi[2] - Xj[2]) ** 2) / (ra / 2) ** 2)
        potential[i] += value
        potential[j] += value
max_potential_value = max(potential)  # p1
max_potential_index = potential.index(max_potential_value)

# filter through accept and reject criteria
current_max_value = max_potential_value
criteria = 1
while criteria and current_max_value:
    criteria = 0
    max_potential_vector = normalized_data_matrix[max_potential_index]  # x1
    potential_ratio = current_max_value / max_potential_value  # Pk and MaxPValue

    if potential_ratio > Eup:
        criteria = 1
    elif potential_ratio > Edown:
        dmin = np.min([(max_potential_vector[0] - cc[0]) ** 2 + (max_potential_vector[1] - cc[1]) ** 2 +
                       (max_potential_vector[2] - cc[2]) ** 2 for cc in cluster_center])
        if ((dmin / ra) + potential_ratio) >= 1:
            criteria = 1
        else:
            criteria = 2
    elif potential_ratio < Edown:
        break

    if criteria is 1:
        cluster_center.append(max_potential_vector)
        for i in range(size):
            Xj = normalized_data_matrix[i]
            potential_value = potential[i]
            potential_value = potential_value - (current_max_value * np.exp(-4.0 *
                                                ((max_potential_vector[0] - Xj[0]) ** 2 +
                                                (max_potential_vector[1] - Xj[1]) ** 2 +
                                                (max_potential_vector[2] - Xj[2]) ** 2)) / (rb / 2) ** 2)
            if potential_value < 0:
                potential_value = 0
            potential[i] = potential_value
        current_max_value = max(potential)  # p1
        max_potential_index = potential.index(current_max_value)
    elif criteria is 2:
        potential[max_potential_index] = 0
        current_max_value = max(potential)  # p1
        max_potential_index = potential.index(current_max_value)

print('Subtractive cluster centers')
print(cluster_center)
"""
