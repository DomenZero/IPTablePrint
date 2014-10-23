from urllib.request import Request
from urllib.request import urlopen
from time import clock
import xlrd
import funcIP
import recinFile
# counts the frequency of occurrence of every word in the 
# text
def searchIPinFile(worksheet, pfile,namefileip):
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = -1
    i=0
    #new write file 
    f = open(pfile, 'w')
    f = open(namefileip, 'w')
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
                    cell_value2 = worksheet.cell_value(curr_row, curr_cell)
            
                    if cell_value2!="":
                        if (funcIP.abcdIp(cell_value2)==True):
                            funcIP.finditerIP(cell_value2,namefileip)
                            if (funcIP.isIp(cell_value2)==True):
                                try:
                                    #add ipdata in file
                                    f = open(pfile, 'a')
                                    f.write(cell_value2+"\n")
                                    f.close()
                                    print ('Row:', cell_value2)
                                except IOError:
                                    print ("No file")
                            else:
                                curr_row += 1
