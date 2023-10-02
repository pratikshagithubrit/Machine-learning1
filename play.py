
from sklearn import tree

def ballpredictor():
    Features=[[35,1],[48,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Lables=[1,1,2,1,2,1,1,1,1,1,2,1,2,1,2]

    obj=tree.DecisionTreeClassifier()

    obj=obj.fit(Features,Lables)
    ret=obj.predict([[weight,surface]])
    if ret ==1:
        print("your object looks like Tennis ball")
    else:
         print("your object looks like Cricket ball")


def main():
    print("_________ball case study________")

    print("please enter the  weight of your object in grams")
    weight=int(input())
    print("please enter type of surface of your object(Rough/Smooth)")
    surface=input()
    if surface.lower()=="rough":
        surface=1
    elif surface.lower()=="smooth":
        surface=0
    else:
        print("invalid type of surface")
        exit()
    ballpredictor(weight,surface)

if __name__ == "__main__":
    main()