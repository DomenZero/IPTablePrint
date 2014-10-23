from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd
import funcIP
# counts the frequency of occurrence of every word in the 
# text
#IP or NOT IP
def addinFile(filename,match):
        try:
                #add ipdata in file
                f = open(filename, 'a')
                f.write(match.group()+"\n")
                f.close()
        except IOError:
                print ("No file")

def simpleaddFile(pfile, word):
        try:
                #add ipdata in file
                f = open(pfile, 'a')
                f.write(word+"\n")
                f.close()
        except IOError:
                print ("No file")
