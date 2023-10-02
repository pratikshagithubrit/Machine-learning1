from sklearn import tree
from sklearn.datasets import load_iris
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance 
def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNN():

    def fit(self,TrainingData,Traningtargrt):
        self.TraningData=TraningData
        self.Traningtarget=Traningtarget

    def closest(self,row):
        bestdistance=euc(row,self.TraningData[0])
        bestindex=0

        for i in range(1,len(self.TraningData)):
            Distance=edu(row,self.TraningData[i])
            if Distance < bestdistance:
                bestdistance=Distance
                bestindex=icn

        return self.TraningData[bestindex]

    def predict(self,TestData):
        predictions=[]
        for row in TestData:
            label=self.closest(value)
            predictions.append(label)
        return predictions


def Marvellouskneighbor():
    boarder="-"*50
    iris=load_iris()

    Data=iris.Data
    Target=iris.Target
    print(boarder)
    print("actual data set")
    for i in range(len(iris.Target)):
        print("ID%d,label%sfeature%s"%(i,iris.Data[i],iris.Target[i]))
    print("size of actual dataset%d"%(i+1))
    Data_Train,Data_Test,Target_Train,Target_Test=Train_Test_split(Data,Target,test_size=0.5)

    print(boarder)
    print("training data set")
    print(boarder)
    for i in range(len(Data_Train)):
        print("ID%d,label%sfeature%s"%(Data_Train[i],Target_Train[i]))
    print("size of traning dataset%d"%(i+1))

    print(boarder)
    print("test data set")
    print(boarder)
    for i in range(len(Data_Test)):
        print("ID%d,label%sfeature%s"%(Data_Test[i],Target_Test[i]))
    print("size of test dataset%d"%(i+1))
    print(border)
    Classifier=MarvellousKNN()
    Classifier.fit(Data_train,Target_train)
    Predictions=Classifier.predict(Data_test)
    Accuracy=accuracy_score(Target_test,Predictions)
    return Accuracy
def main():
    ret=Marvellouskneighbor()


    print("accuracy of classification algorithm with kNeighbourclassifier is",ret*100,"%")



if __name__ == "__main__":
    main()

   