#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing iris dataset with pandas
datsset=pd.read_csv('iris.csv')
x=dataset.iloc[:,[0,1,2,3]].values
#finding the optium number of cluster of k mean classfin
from sklearn.cluster import KMeans
wcss=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

#plotting the result onto line grapg,allowing user observe'elbow'
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.title('number of cluster')
plt.ylabel('wcss')#within cluster sum of squares 
plt.show()

#applying kmeans to dataset/creating kmeans classifier
kmeans=KMeans(n_clusters=3,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans=kmneans.fit_predict(x)

#visulising the cluster
plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100,c='red',label='Iris-setosa')
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100,c='blue',label='Irs-versicolour')
plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=100,c='green',label='Iris-virginica')

#plotting centroid of cluster
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_[:,1],s=100,c='yellow',label='Centroids')
plt.legend()
plt.show()
