from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def MarvellousSVM():
    #load data
    cancer=datasets.load_breast_cancer()

    #print no. 13 feature
    print("features of cancer datasts",cancer.feature_names)

    ##print no. 13 labels
    print("labels of cancer datasts",cancer.feature_names)

    print("Shape of datasets",cancer.data.shape)

    print("first 5 records")
    print(cancer.data[0.5])

    #0:maligant,1:beginn
    print("target of datasets",cancer.target)

    x_train,x_test,y_test,y_train=train_test_split(cancer.data,cancer.target,random_state=109,test_size=0.3)

    clf=svm.SVC(kernel='linear')#linear kernel
    #trainning 
    clf.fit(x_train,y_train)

    #responce datasets
    y_pred=clf.predict(x_test)

    #accurcy check
    print("accuracy of model",metrics.accuracy_score(y_test,y_pred)*100)

def main():
    print("_________marvellous_________")

    MarvellousSVM()

if __name__ == "__main__":
    main()
