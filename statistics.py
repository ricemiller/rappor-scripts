#!/usr/bin/env python2

"""Creates a CSV file that offers statistics about the results, as the amount of strings found with a determined margin of error (delim1, delim2 and delim3).
Input: comparison.csv delim1 delim2 delim3
Output: statistics.csv (stdout)
"""

import csv
import sys

if len(sys.argv) != 5:
    print ("Usage: statistics.py comparison.csv delim1 delim2 delim3 > statistics.csv")
    print ("delim1, delim2 and delim3 should be numbers between 0 and 100 and it should be the maximum percent threshold allowed to sum the amount of found strings.")
    sys.exit(1)

comparison = sys.argv[1]
delim1 = int(sys.argv[2])
delim2 = int(sys.argv[3])
delim3 = int(sys.argv[4])


ifile = open(comparison, "rb")
reader = csv.reader(ifile)
writer = csv.writer(sys.stdout)
rownum = 0
numRowsDelim1=0
numRowsDelim2=0
numRowsDelim3=0

for row in reader:
    if rownum == 0:
        writer.writerow(("strings_found", str(delim1) + "%_error",str(delim2) + "%_error",str(delim3) + "%_error"))
    else:
        if int(row[1]) > 0:
            proportion = float(row[2]) / float(row[1]) * 100
            if (proportion > (100 - delim1)) and (proportion < (100 + delim1)):
                numRowsDelim1 += 1
            if (proportion > (100 - delim2)) and (proportion < (100 + delim2)):
                numRowsDelim2 += 1
            if (proportion > (100 - delim3)) and (proportion < (100 + delim3)):
                numRowsDelim3 += 1

    rownum +=1
ifile.close()
writer.writerow((rownum,numRowsDelim1,numRowsDelim2,numRowsDelim3))
exit(0)
