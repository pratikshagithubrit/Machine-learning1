import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plt

def MarvellousKMean():
    print("__________________")
    #set three centers model should predict similiar results
    center_1=np.array([1,1])
    print(center_1)
    print("______________")
    center_2=np.array([5,5])
    print(center_2)
    print("_________________")
    center_3=np.array([8,1])
    print(center_3)
    print("________________")

    #generate random data and center to three centers
    data_1=np.random.randn(7,2)+center_1
    print("elements of second cluster with size"+str(len(data_1)))
    print(data_1)
    print("____________")


    data_2=np.random.randn(7,2)+center_2
    print("elements of second cluster with size"+str(len(data_2)))
    print(data_2)
    print("____________")

    data_3=np.random.randn(7,2)+center_3
    print("elements of second cluster with size"+str(len(data_3)))
    print(data_3)
    print("____________")

    data=np.concatenate((data_1,data_2,data_3),axis=0)
    print("size of complete data set"+str(len(data)))
    print(data)
    print("____________")

    plt.scatter(data[:,0],data[:,1],s=7)
    plt.title('marvellous infosystem:input dataset')
    plt.show()
    print("___________________")

    #no.of cluster
    k=3

    #no.of traning data
    n=data.shape[0]
    print("total number of elements are",n)
    print("_________________")

    #no.of feature in data
    c=data.shape[1]
    print("total number of features are",c)
    print("________________")

    #generate random centers use sigma and mean to ensure reprsent the whole data
    std=np.mean(data,axis=0)
    print("value of mean",mean)
    print("_______________")

    #calculate standard devation
    std=np.std(data,axis=0)
    print("value of std",std)
    print("_______________")
    centers=np.random.randn(k,c)*std+mean
    print("random points are",centers)
    print("_____________")

    #plot data and the centers genertaed as random
    plt.scatter(data[:,0],data[:,1],c='r',s=7)
    plt.scatter(centers[:,0],centers[:,1],marker="*",c='g',s=150)
    plt.title('marvellous infosystems:input dataset with random centroid *')
    plt.show()
    print("____________________")

    centers_old=np.zeros(centers.shape) #to store old centers
    centers_new=deepcopy(centers) #store new centers

    print("values of old centroids")
    print(centers_old)
    print("_______________")

    print("values of new centroids")
    print(centers_new)
    print("_______________")

    data.shape
    clusters=np.zeros(n)
    distance=np.zeros((n,k))

    print("initial distances are")
    print(distances)
    print("________________")

    erroe=np.linalg.norm(centers_new-centers_old)
    print("value of error",error)

    #when update the estimate centers stays same exit loop
    while error !=0:
        print("value of error is",error)
        
        #measure the distance every center

        print("measure distance to every center")
        for i in range(k):
            print("iteration number",i)
            distances[:,i]=np.linalg.norm(data-centers[i],axis=1)

    #all traning data to closet center
        clusters=np.argmin(distance,axis=1)

        centers_old=deepcopy(centers_new)

        #calculate every cluster and update center
        for i in range(k):
            centers_new[i]=np.mean(data[clusters==i],axis=0)
        error=np.linalg.norm(centers_new-centers_old)

        #end of while

    centers_new

        #plot data and the centers generted random
    plt.scatter(data[:,0],data[:,1],s=7)
    plt.scatter(centers_new[:,0],centers_new[:,1],market='*',c='g',s=150)
    plt.title('marvellous infosystem:final data with centroid')
    plt.show()

def main():
    print("_________marvellous infosystem__________")

    print("clustering using k mean algorithm")
    MarvellousKMean()

if __name__ == "__main__":
    main()