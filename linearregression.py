import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousHeadBrainPredictor():

    #load data
    data=pd.read_csv('MarvellousHeadBrain.csv')
    print("size if data set",data.shape)
    X=data['Head size(cm^3)'].values
    Y=data['Brain Weight(grams)'].values

    #least square method
    mean_x=np.mean(X)
    mean_y=np.mean(Y)

    n=len(X)#length find

    numerator=0#varch
    denomenator=0#ghalch

    #eqn line y=mx+c
    for i in range(n):#i chi 0 to 4 0 pasun ka tr list ahe
        numerator+=(X[i]-mean_x)*(Y[i]-mean_y)#(x-xbar)(y-ybar)
        denomentor +=(X[i]-mean_X)**2#(x-xbar)^2

    m=numerator/denomenator
    c=mean_y-(m*mean_x) #find mean
    print("slope of regression line is",m)
    print("Y intercept of regression lie is",c)

    max_x=np.max(X)+100
    min_x=np.min(X)-100

    #display plottng above points
    x=np.linespace(min_x,max_x,n)

    y=c+m*X

    plt.plot(x,y,color='#58b970',label='regression line')
    plt.scatter(X,Ycolor='#ef5423',label='scatter plot')

    plt.xlabel('head size in cm3')
    plt.ylabel('brain weight in gram')

    plt.legend()
    plt.show()

    #findout goodness of fit R square(0 to 1 value constant asti)
    ss_t=0
    ss_r=0

    for i in raange(n):
        y_pred=c+m*X[i]
        ss_t +=(Y[i]-meam_y)**2
        ss_r +=(Y[i]-y_pred)**2

    r2=1-(ss_r/ss_t)
    print(r2)

def main():
    print("________marvellous family______")
    print("supervised Machine learning")
    print("liner regression on head and Bbrain size of data set")
    MarvellosHeadBrainPredictor()

if __name__ == "__main__":
    main()
