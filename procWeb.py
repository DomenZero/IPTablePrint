from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd

def getWebPage( url ):

    req = Request( url )

    print( "Requesting Web file at", url )

    encoding = 'iso-8859-1'  
    text = urlopen( req ).read().decode( encoding )
    
    print( "Done! Received %d characters." % len( text ) )

    return text
