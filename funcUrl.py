#connect library
import urllib
from urllib.request import urlopen

def addinFile(url, i):
    #system action
    print ("downloading with urllib")
    #save Internet file
    urllib.request.urlretrieve(url, i+".html")
