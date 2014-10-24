from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd
#open library
import funcIP
import procWeb
import procFile
import funcUrl
import recinFile
import procText
#open table

def main():
    #vstavka koda
    nametable="test.xls"
    workbook = xlrd.open_workbook(nametable)
    #select table page
    namepage="2014"
    worksheet = workbook.sheet_by_name(namepage)
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = -1
    i=0
    #Save IP in 
    procFile.searchIPinFile(worksheet,"Printip.txt","ggg.txt")
    #mas 04.09
    mas=[]
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        curr_cell = -1
        while curr_cell < num_cells:
            i=i+1
            curr_cell += 1
            cell_type = worksheet.cell_type(curr_row, curr_cell)
            cell_value = worksheet.cell_value(curr_row, curr_cell)
            if cell_value=="IP":
                while curr_row < num_rows:
                    curr_row += 1
                    row = worksheet.row(curr_row)
        #print ('Row:', curr_row)\
                    cell_value2 = worksheet.cell_value(curr_row, curr_cell)
                    if cell_value2!="":
                        print ('Row:', cell_value2)
                        if (funcIP.isIp(cell_value2)==True):
                            url = "http://"+cell_value2+"/t_gen.htm"
                            print(url)
                            #url = "http://autorist.ru"
                            text = procWeb.getWebPage( url )
                            #print( "Number of words in document = %d\n\n" % len( text.split() ))
                            #freq = {}
                            

                            #часть с закачкой 01.09
                            numf="name"
                            funcUrl.addinFile(url,numf)

                            
                            
                            #for word in tecell_value2xt.split():
                            # print (' ', cell_type, ':', cell_value)
                            #vstavka koda
                            f = open("text.txt", 'w')
                            mas=text.split()
                            i_in_mas=0
                            for word in text.split():
                               # print(word)
                                i_in_mas=i_in_mas+1
                                
                                recinFile.simpleaddFile("text.txt", word)
                                if(word=="Sheets"):
                                    #print(text.split())
                                    #print(word)
                                    #recinFile
                                    procText.searchText(mas, i_in_mas)
                                    #print (mas[i_in_mas])

    # find the most frequent word in the text
    start = clock()
    tuples = procText.countFrequencies( text )
    end   = clock()
    for count, word in tuples:
        print( "most frequent top-10 word \"%5s\" appeared %d times" % (word, count) )

    print( "\nelapsed time using a dictionary = %1.3f seconds\n" % (end-start ) )   

main()
#print (isIp("192.168.0.1"))
