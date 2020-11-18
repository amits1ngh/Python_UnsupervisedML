import matplotlib.pyplot as plt 
from matplotlib import style
from sklearn.cluster import KMeans
import numpy as np

style.use('ggplot')
data_set = np.array([[1,2],[3,2],[3,2],[1.2,2.5],[7,8],[8,9],[8,7],[7,6]])

# plt.scatter(data_set[:,0],data_set[:,1], s=150)
# plt.show()

clf = KMeans(n_clusters=2)
clf.fit(data_set)

centroids = clf.cluster_centers_
labels = clf.labels_

color_list =2*["g.","r.","b.","c.","k.","c."]

for i in range(len(data_set)):
    plt.plot(data_set[i][0],data_set[i][1], color_list[labels[i]], markersize= 10)

plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidths=5)
plt.show()


