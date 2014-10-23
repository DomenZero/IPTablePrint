from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd
# counts the frequency of occurrence of every word in the 
# text
def countFrequencies(text):
    # create dictionary: key = word, value = count 
    freq = {}  

    # count each word in the text
    for word in text.split():
        try:
            freq[word] += 1
        except KeyError:
            freq[word] = 1

    tuples = [ (count,word) for word,count in freq.items() ]
    tuples.sort()
    return tuples[-10:]

def analizeHtml(text):
    #result = re.findall(c, ip)
    #print(result)
    #{[^}\n]+}
    #result = re.finditer(r'[\d]+[.]+[\d]+[.]+[\d]+[.]+[\d]', ip)
    #<td valign=top width=130><font class=s2 face="Arial,Helvetica" size=2>
    result = re.finditer(r'["<td"]+[\w]+[\w]+[\w]+[\d]+', ip)
    for match in result:
        print(match.group())
        recinFile.addinFile(namefileip, match)

def searchText(mas, i):
    k=0
    #ik=0
    #for ik in mas:
    while k < 7:
        print(mas[i+k])
        k=k+1
    #while  i<=i+7:
       # print(mas[i])
     #   i=i+1
