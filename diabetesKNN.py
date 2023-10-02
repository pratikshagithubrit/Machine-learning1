import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

print("_________marvellous infosystem__________")
print("________diabetes predictor using KNN_________")
diabetes=pd.read_csv('diabetes.csv')

print("column of dataset")
print(diabetes.columns)

print("first 5 records of dataset")
print(diabetes.head())

print("diamension of diabetes data:{}".format(diabetes.shape))

x_train,x_test,y_train,y_test=train_test_split(diabetes.loc[:,diabetes.columns!='outcome'],diabetes['outcome'],stratify=diabetes['outcome'],random_state=66)

tranning_accuracy=[]
test_accuracy=[]

#try n_neighbors in neighbors_setting 1 to 10
neighbors_setting=range(1,11)
for n_neighbors in neighbors_setting:
    #build model
    knn=KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(x_train,y_train)

    #record tranning set accurcy
    tranning_accuracy.append(knn.score(x_train,y_train))

    #record test set accuracy
    test_accuracy.append(knn.score(x_test,y_test))

    plt.plot(neighbors_setting,tranning_accuracy,label="tranning accuracy")
    plt.plot(neighbors_setting,test_accuracy,label="test accuracy")
    plt.ylabel("accuracy")
    plt.xlabel("n_neighbors")
    plt.legend()
    plt.saveflg('knn_compare_model')
    plt.show()

    knn.fit(x_train,y_train)

    print('accuracy of knn classifier tranning set:{.2f}'.format(knn.score(x_train,y_train)))

    print('accuracy of knn classifier test set:{.2f}'.format(knn.score(x_test,y_test)))










