import numpy as np
import pandas as pd
from sklearn import preprocessing  #process jaych adhi kai process karychi asal tr
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):
    #1load data
    data=pd.read_csv(data_path,index_col=0)
    print("size of actual data set",len(data))

    #2data clean
    feature_names=['Whether','Temperature','Play']
    print("names of features",feature_names)
    Whether=data.Whether
    Temperature=data.Temperature
    Play=data.Play

    #creating labelencoder
    le=preprocessing.LabelEncoder()

    #converting string labels into numbers
    Whether_encoded=le.fit_transform(Whether)
    print(Whether_encoded)

    #converting string labels into numbers
    temp_encoded=le.fit_transform(Temperature)
    label=le.fit_transform(Play)
    print(temp_encoded)

    #combining wether,temp into single list of tuples
    features=list(zip(Whether_encoded,temp_encoded))

    #3train data
    model=KNeighborsClassifier(n_neighbors=3)

    #train the model in tranning data sets
    model.fit(features,label)

    #4 test data
    predicted=model.predict([[1,2]])#0:overcast,2:mild
    print(predicted)
    if(predicted==1):
        print("its play")
    else:
        #if(predicted==2):
        print("dont play")

def main():
    print("machine learning application")
    print("play predictor using K Nearest Kneighbor algorithm")


    MarvellousPlayPredictor("PlayPredictor.csv")


if __name__ == "__main__":
    main()
