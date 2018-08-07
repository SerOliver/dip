import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

def preporuka():

    #importing dataset with pandas
    dataset = pd.read_csv('basketball.dat')  # [0:50]
    x = dataset.iloc[:, [3, 1]].values
    print(x)

    wcss = []

    #elbow calculation / optimum number of clusters
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, init='k-means++',
                        max_iter=300, n_init=10, random_state=0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)

    kmeans = KMeans(n_clusters=2, init='k-means++',
                    max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(x)

    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1],
                s=100, c='red', label='Player Age')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1],
                s=100, c='blue', label='Player H')
    #plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1],
    #            s=100, c='green', label='Ash')
    #plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1],
    #            s=100, c='magenta', label='Magnesium')

    #Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[
                :, 1], s=100, c='yellow', label='Centroide')

    #plt.plot(range(1, 10), wcss)
    plt.xlabel('Player Age')
    plt.ylabel('Player H')  # within cluster sum of squares
    plt.legend()
    plt.show()

    return x
