import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

simplefilter(action='ignore',category=FutureWarning)

print("_________marvellous infosystem__________")
print("________diabetes predictor using logisticRegression_________")
diabetes=pd.read_csv('diabetes.csv')

print("column of dataset")
print(diabetes.columns)

print("first 5 records of dataset")
print(diabetes.head())

print("diamension of diabetes data:{}".format(diabetes.shape))

x_train,x_test,y_train,y_test=train_test_split(diabetes.loc[:,diabetes.columns!='outcome'],diabetes['outcome'],stratify=diabetes['outcome'],random_state=66)

logreg=LogisticRegression().fit(x_train,y_train)



print("accuracy of traning set:{:.3f}".format(logreg.score(x_train,y_train)))

print("accuracy of test set:{:.3f}".format(logreg.score(x_test,y_test)))

logreg001=LogisticRegression(C=0.01).fit(x_train,y_train)
tree.fit(x_train,y_train)

print("accuracy of traning set:{:.3f}".format(logreg001.score(x_train,y_train)))

print("accuracy of test set:{:.3f}".format(logreg001.score(x_test,y_test)))

