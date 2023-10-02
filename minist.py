import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

data=pd.read_csv('minist.csv')

df_x=data.iloc[:,1:]#labels
df_y=data.iloc[:,0]#pixels

x_train,x_test,y_test,y_train=tarin_test_split(df_x,df_y,test_size=0.2,random_state=4)

obj=DecisionTreeClassifier(__,____,____)
adb=AdaBoostClassifier(obj,n_estimators=_____,learaning_rate=_____)
adb=AdaBoostClassifier(DecisionTreeClassifier(),n_estimeters=100,learning_rate=1)
abd.fit(x_train,y_train)
print("testing accuracy using bagging classifier:",abd.score(x_test,y_test)*100)
print("testing accuracy using bagging classifier:",abd.score(x_train,y_train)*100)