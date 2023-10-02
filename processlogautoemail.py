import os
import time
import psutil
import urllib3
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib2.urlopen('https://216.58.192.142',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(filename,time):
    try:
        fromaddr="pp1916581@gmail.com"
        toaddr="op24791@gmail.com"

        msg =MIMEMultipart() #multimedia part ahe tho eka media mhadun dusarya media madey data transfer karto

        msg['from']=fromaddr
        msg['TO']=toaddr

        body="""
        hello%s,
        welcome to IT industries.
        please find attched document which contain Log of Running process.
        Log file is created at:%s

        this is auto gennerted mail.

        Thanks
        pratiksha pawar
        baramti(pune)
        """%(toaddr,time)

        subject="""
        Marvellous Infosystem Process log Generted :%s
        """%(time)

        msg['Subject']=subject
        msg.attchment=open(filename,"rb")

        p=MIMEBase('application','octet-stream')
        p.set_payload((attchment).read())#payload meaning the attchmdement keli jayt  eg..ekdhi person ek jagayvarun dusarya jagayvar janar asal kahitari anaysadi tr tyla peshvi den
        
        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attchment;filename=%s"%filename)

        msg.attch(p)

        s=smtplib.SMTP('smtp.gmail.com',587)#587 is text code

        s.starttls()

        s.login("pp1916581@gmail.com","Pawar@19")

        text=msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit() #quite mhanjay band karynay script

        print("log file successfully send through mail")

    except Exception  as E:
        print("unable to send mail",E)

def ProcessLog(log_dir='Marvellous'):
    listprocess=[]

    if not os.path.exsits(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    seprator="-"*80


    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f=open(log_path,'w')
    f.write(seprator+"\n")
    f.write("marvellous infosystem process logger"+time.ctime()+"\n")
    f.write(seprator+"\n")
    f.write("\n")

    for proc in psutil.process.iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','usename'])
            vms=proc.memory_info()>vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

    #print("Log file is successfully generated at location %s",%(log_path))
    connected=is_connected()

    if connected:
        starttime=time.time()
        MailSender(log_path,time.ctime())
        endtime=time.time()

        print('took %s second send mail%s',(endtime-starttime))

    else:
        print("there is no internet connection")

def main():
    print("___________marvellous_____________")
    print("application name:"+argv[0])

    if(len(argv)!=2):
        print("error:invalid number argument")
        exit()

    if(argv[1]=="-h"):
        print("this script used to log record running process")
        exit()

    if(argv[1]=="-h"):
        print("usage:application name absolutepath_of_dirctory")
        exit()

    try:
        scedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            scedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error:invalid data type")

    except Exception as E:
        print("error:invalid path")

if __name__ == "__main__":
    main()


