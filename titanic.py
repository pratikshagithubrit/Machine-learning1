import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as mpl
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def MaevellousTitanicLogistic():
    #1:load data
    titanic_data=pd.read_csv('MarvellousTitanicDataset.csv')

    print("first 5 entries from loaded dataset")
    print(titanic_data.head())

    print("number of passenger are"+str(len(titanic_data)))

    #2:anlyze data
    print("visulization:survived and non survived passenger")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target).set_title("Marvellous infosystem:Survied and non survied passenger")
    show()

    print("visulization:survied and non survied passenger based on gender")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue="sex").set_title("marvellous infosystem:survied and non survied passenger based on gender")
    show()

    print("visulization:survived and non survived  passenger based on passenger class")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue="Pclass").set_title("marvellous infosystem:survived and non survived passenger based on the passenger class")
    show()

    print("visulization:survived and non survived passenger based on passenger age")
    figure()
    titanic_data["Age"].plot.hist().set_title("marvellous iinfosystem:survived and non survived passenger based on passenger age")
    show()

    print("visulization:survived and non survived passenger based on passenger on the Fare")
    figure()

    titanic_data["Fare"].plot.hist().set.title("marvellous infosystem:survived and non survived passenger based on Fare")
    show()

    #3:data cleanning
    titanic_data.drop("zero",axis=1,inpalce=True)

    print("first 5 entries loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("values of sex column")
    print(pd.get_dummies(titanic_data["sex"]))

    print("value of sex column after removing one field")
    sex=pd.get_dummies(titanic_data["sex"],drop_first=True)
    print(sex.head(5))

    print("value of Pclass column after removing one field")
    Pclass=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(Pclass.head(5))

    print("value of data data set after concatenating new columns")
    titanic_data=pd.concat([titanic_data,sex,Pclass],axis=1)
    print(titanic_data.head(5))

    print("value of data data set after removing irrelevent columns")
    titanic_data=pd.drop(["sex","sibsp","Parch","Embarked"],axis=1,inpalce=True)
    print(titanic_data.head(5))

    x=titanic_data.drop("survived",axis=1) 
    y=titanic_data["survived"] 

    #4:data traning
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5) 
    logmodel=LogisticRegression()
    logmodel.fit(xtrain,ytrain) 

    #4:data testing
    prediction=logmodel.predict(xtest)

    #5:calculate accurcy
    print("classification report of logistic regression is")
    print(classification_report(ytest,prediction))

    print("confusion matrix of logistic regression is")
    print(confusion_report(ytest,prediction))

    print("accuracy  of logistic regression")
    print(accuracy_score(ytest,prediction))

def main():
    print("________________marvellous infosystem________________")
    print("survived ML")
    print("Logistic regression on tatanic dataset")

    MarvellousTitanicLogistic()

if __name__ == "__main__":
    main()

    

    