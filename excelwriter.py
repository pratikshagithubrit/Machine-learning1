import os
import fnmatch
from sys import *
import xlsxwriter

def ExcelCreate(name):
    workbook=xlsxwriter.Workbook(name)

    worksheet=workbook.add_worksheet()

    worksheet.write('A1','Name')
    worksheet.write('B1','MailID')
    worksheet.write('C1','Age')
    worksheet.write('D1','Birth_date')
    workbook.close()

def main():
    print("_______marvellous infosystem_____")
    print("application name:"+argv[0])
    if(len(argv)!=2):
        print("error:invalid number of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("this  script used to create excel file and write data into it")
        exit()

    if(argv[1]=="-u"):
        print("usage:applicationname Name_of_file")
        exit()

    try:
        ExcelCreate(argv[1])

    except Exception:
        print("Error:Invalid input")

if __name__ == "__main__":
    main()

   