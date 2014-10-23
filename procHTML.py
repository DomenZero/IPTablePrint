from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd
# getWebPage(): given a URL will go grab the content of the page
# and return it as a string.
def getWebPage( url ):

    req = Request( url )

    print( "Requesting Web file at", url )

    encoding = 'iso-8859-1'  # can sometimes be 'utf-8'
    text = urlopen( req ).read().decode( encoding )
    
    print( "Done! Received %d characters." % len( text ) )

    return text

def annaHTML(pfile):
    if ("Total Sheets Delivered"):
        f = open(pfile, 'r')
        #f.write(cell_value2+"\n")
        f.close()
	
