#below application demonstate  we can create wine predictor using pandas

from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    #load dataset
    wine=datasets.load_wine()

    #print the names of features
    print(wine.feature_names)

    #print label species(0:class_0,1:class_1,2:class_2)
    print(wine.target_names)

    #print wine data (5 records)
    print(wine.data[:20])

    #print the wine labels(0:class_0,1:class_1,2:class_3)
    print(wine.target)

    #split dataset tranning and test set 70 and 30 test size in test data
    x_train,x_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.3)

    #create knn classifier
    knn=KNeighborsClassifier(n_neighbors=3)

    #train the model using the training sets
    knn.fit(x_train,y_train)

    #predict rsponce for test dataset
    y_pred=knn.predict(x_test)

    #model accuracy often the classifier correct?
    print("accuracy",metrics.accuracy_score(y_test,y_pred))

def main():
    print("_____marvellous infosystem______")
    print("wine predictor application using knn")
    WinePredictor()

if __name__ == "__main__":
    main()