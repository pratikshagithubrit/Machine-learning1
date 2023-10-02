import pandas as pd
from sklearn import preprocessing
#from sklearn neighbors import sklearnKNeighborsClassifier
def MarvellousFaceMaskDetector(data_path):

    print("[info]loading face detector model")
    prototxtpath=os.path.sep.join([args["face"],"deploy.prototxt"])
    weightspath=os.path.sep.join([args["face"],"res10_300x300_ssd_iter_140000.caffemodel"])
    faceNet=cv2.dnn.readNet(prototxtpath,weightspath)

    print("[info]loading face mask detector model...")
    maskNet=load_model(args["model"])

    print("[info]starting video stream...")
    vs=videostream(src=0).start()
    time.sleep(2.0)

    for(box,pred) in Zip (locs,preds):
        (startX,startY,endX,endY)=box
        (mask,withoutmask)=pred

    label="mask"
    if mask>withoutmask else("no mask")
        
    color = (0,255,0)
    if label=="mask"else(0,0,255)

    label="{}:{:.2f}%".format(label,max(mask,withoutmask)*100)

    cv2.puttext(frame,label(startX,startY),(endX,endY),color,2)

def main():
    print("machine learning application")
    print("facemask detector case sutdy")
    MarvellousFaceMaskDetector("deploy.prototxt")
if __name__ == "__main__":
    main()

    

   