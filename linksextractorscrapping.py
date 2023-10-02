import os
import bs4
import requests
from sys import *

def MarvellousDisplay(URL):
    res=requests.get(URL)
    print(type(res))

    soup=bs4.BeautifulSoup(res.text,'lxml')
    print(type(soup))

    links=soup.find_all('a',href=True)
    return links

def main():
    print("______________marvellous__________________")
    print("applicatio_name"+argv[0])

    if(len(argv)==2):
        if(argv[1]=="-h"):
            print("script used to fetch links from wikipedia file")
            exit()

        if(argv[1]=="-u"):
            print("uasge:application name")
            exit()
    
    url="https://en.wikipedia.org/wiki/Python_(programming_languvage)"
    arr=MarvellousDisplay(url)
    print("links are")

    for element in arr:
        if"#"not in element['href']:
            print(element['href'])
if __name__ == "__main__":
    main()          
