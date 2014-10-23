#library IP
from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd
import re
import string
import recinFile

#IP or NOT IP
def isIp(ip):
    log=True
    octets = ip.split(".")
    pattern = re.compile(r'\[a-z]')
    if (isinstance(octets, int )==True): # True
        for octet in octets:
            if (255<int(octet) or int(octet)<0 or len(octets)!=4):
                log = False
                break
    return log
#код прошел тестирование по наличию текстовых комбинаций в ячейке
def abcdIp(ip):
    c = re.compile(r'\b^[a-z]')
    tuples = re.findall(c, ip)
    if tuples:
        log=False
    else:
        log=True
    return log

#код прошел тестирование по маске
def finditerIP(ip, namefileip):
    #result = re.findall(c, ip)
    #print(result)
    #{[^}\n]+}
    #result = re.finditer(r'[\d]+[.]+[\d]+[.]+[\d]+[.]+[\d]', ip)
    result = re.finditer(r'[\d]+[.]+[\d]+[.]+[\d]+[.]+[\d]+', ip)
    for match in result:
        print(match.group())
        recinFile.addinFile(namefileip, match)
       # try:
            #add ipdata in file
       #     f = open("ggg.txt", 'a')
       #     f.write(match.group()+"\n")
       #     f.close()
       # except IOError:
       #     print ("No file")

  #  for match in result:
   #     print(match.group())

    
    #        log=True 
    #return log
