from bs4 import *
import requests
import os

def folder_create(images):
    try:
        folder_name=input("enter folder name")
        os.mkdir(folder_name)

    except:
        print("folder exit with that name")
        folder_create(images)

        download_images(images,folder_name)

def download_images(images,folder_name):
    count=0

    print(f"total{len(images)}Image found")

    if len(images)!=0:
        for i,image in enumerate(images):

            try:
                image_link=image["data-srcset"]
            except:
                try:
                    image_link=image["data-fallback-src"]
                except:
                    try:
                        image_link=image["src"]

                    except:
                        pass
            try:
                r=requests.get(image_link).content
                try:
                    r=str(r,'utf-8')
                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpg","wb+")as f:
                        f.write(r)
                        count +=1

            except:
                pass
        if count == len(images):
            print("all images download")
        else:
            print("total{count}images download out of {len(images)}")
def main():
    print("___________marvellous infosystem__________")
    print("application name:auto image download")

    url=input("enter URL from where you want download images")
    r=requests.get(url)

    soup=BeautifulSoup(r.text,'html.parser') 
    images=soup.findAll('img')
    folder_create(images) 

if __name__ == "__main__":
    main()         
