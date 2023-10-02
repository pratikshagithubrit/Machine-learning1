from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
#import train test split
from sklearn.model_selection import train_test_split
#scikit learn accuracy calculation
from sklearn import metrics

#load data
iris=datasets.load_iris()
x=iris.data
y=iris.target

#split dataset traning set and test set
x_train,x_test,y_test,y_train=train_test_split(x,y,test_size=0.3)

#create adbboost classifier object
abc=AdaBoostClassifier(n_estimators=50,learning_rate=1)

#tain ababoost classifier
model=abc.fit(x_train,y_train)

#predict rsponce(x_test)
y_pred=model.predict(x_test)

print("accuracy",metics.accuracy_score(y_test,y_pred))