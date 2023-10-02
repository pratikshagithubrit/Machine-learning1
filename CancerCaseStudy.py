#####################################################
#requried python package

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

############################################################
#file paths
#############################################################
INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH == "breast-cancer-wisconsin.csv"

#############################################################
#function_name:read_data
#Description:read data into pandas dataframe
#input:path of csv
#output:gives data
#author:________________
#Date:____________
##########################################################
def read_data(path):
    data=pd.read_csv(path)
    return data

###########################################################
#function_name:get_headers
#Description:dataset headers
#input:dataset
#output:reurn the header
#author:________________
#Date:____________
###########################################################

def get_headers(dataset):
    return dataset.columns.values

###########################################################
#function_name:add_headers
#Description:add the headers to the dataset
#input:dataset
#output:updated dataset
#author:________________
#Date:____________
###########################################################

def add_headers(dataset,headers):
    dataset.columns=headers
    return dataset

###########################################################

#function_name:data_file_to_csv
#input:nothing
#output:write data csv
#author:________________
#Date:____________
###########################################################

def data_file_to_csv():
    #headers
    headers=["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithllalSize","BareNuclei","BlandChromathin","NormalNucleoli","Mitoses","CancerType"]

    #load dataset into pandas data frame
    dataset=read_data(INPUT_PATH)

    #add dataset into headers loaded dataset
    dataset=add_headers(dataset,headers)

    #save the loaded dataset into csv format
    dataset.to_csv(OUTPUT_PATH,index=False)
    print("File saved......!")

#############################################################
#function_name:split_dataset
#Description:split the dataset with train percentage
#input:dataset with related information
#output:dataset after splliting
#author:________________
#Date:____________
#############################################################

def split_dataset(dataset,train_percentage,feature_headers,target_header):
    #split datset inti train and test dataset
    train_x,test_x,train_y,test_y=train_test_split(dataset[feature_headers],dataset[target_headers],train_size=train_percentage)

    return train_x,test_x,train_y,test_y

#################################################################
#function_name:handel_missing_values
#Description:read data into pandas dataframe
#input:dataset with missing values
#output:datset with removing values 
#author:________________
#Date:____________

##################################################################
def handle_missing_values(dataset,missing_values_header,missing_label):
    return dataset[dataset[missing_values_header]!=missing_label]

#################################################################
#function_name:random forest classifier
#Description:to train the random forest clasifier with feature in target data
#author:________________
#Date:____________
####################################################################

def random_forest_classifier(feature,target):
    clf=RandomForestClassifier()
    clf.fit(features,target)
    return clf

#####################################################################
#function_name:data_statictics
#Description:basic statistics of dataset
#input:dataset
#output:description of dataset 
#author:________________
#Date:____________
#####################################################################

def data_statistic(dataset):
    print(dataset.describe())

######################################################################
#function_name:main
#Description:main function from where excution starts
#author:________________
#Date:____________
#######################################################################
def main():
    #load the csv file into pandas dataframe
    dataset=pd.read_csv(OUTPUT_PATH)
    #get statistics loaded daatset
    dataset=handle_misssing_values(dataset,HEADERS[6],'?')
    train_x,test_x,train_x,tarin_y=split_dataset(dataset,0.7,HEADERS[1:1],HEADERS[-1])

    #tarin and test dataset size 
    print("train_x shape::",tarin_x.shape)
    print("train_y shape::",train_.shape)
    print("test_x shape::",test_x.shape)
    print("test_y shape::",test_y.shape)

    #create random forest calssifier instance
    trained_model=random_forest_classifier(train_x,train_y)
    print('trained model::',trained_model)
    predictions=trained_model.predict(test_x)

    for i in range(0,205):
        print("actual outcome{} and predicted outcome{}".format(list(test_y[i],prediction[i])))
        print("train accurcy::",aacuracy_score(test_y,predictions))
        print("test accurcy::",accurcy_matrix(test_y,predictions))
        print("confusion matrix",confusion_matrix(test_y,predictions))

##################################################################################################
#stater
##################################################################################################
if __name__ =="__main__":
    main()
    