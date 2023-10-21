# -*- coding: utf-8 -*-
"""cluster_moons.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/166mwIDC7ptLnr2EoEfY4cBPX-Ks0tg_R
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d2=pd.read_csv("cluster_moons.csv")
d2.head()

from sklearn.preprocessing import StandardScaler
z2= StandardScaler()
d2[["X_1","X_2"]]=z2.fit_transform(d2[["X_1","X_2"]])

from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(d2)
distances, indices = nbrs.kneighbors(d2)
distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.rcParams['figure.figsize'] = 8,8
plt.plot(distances)

from sklearn.cluster import DBSCAN
db2 = DBSCAN(eps = 0.09,min_samples = 10).fit(d2[['X_1','X_2']])
from sklearn.cluster import KMeans
km2 = KMeans(2).fit(d2[['X_1','X_2']]).labels_
dbs2=db2.labels_
plt.scatter(d2['X_1'],d2['X_2'],c=dbs2,cmap='rainbow')
plt.title('DBSCAN')
plt.show()
plt.scatter(d2['X_1'],d2['X_2'],c=km2,cmap='rainbow')
plt.title('Kmeans')
plt.show()

from sklearn.metrics import silhouette_score

silhouette_score(d2[["X_1","X_2"]],km2)

silhouette_score(d2[["X_1","X_2"]],dbs2)

