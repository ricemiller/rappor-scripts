#!/usr/bin/python

"""Associates every client with a cohort, assumes that the dataset is ordered by clients.
Input: m,dataset.csv (client,value)
Output: true_values.csv (client,cohort,value))
"""

import csv
import sys

if len(sys.argv) != 3:
    print ("Usage: true_values_generator.py num_cohorts path_to_dataset.csv")
    sys.exit(1)

m = int(sys.argv[1])
filename = sys.argv[2]


ifile = open(filename, "rb")
reader = csv.reader(ifile)
#########
writer = csv.writer(sys.stdout)
 ######
rownum = 0
client = ""
cohort = -1
for row in reader:
    # Save header row.
    if rownum == 0:
        writer.writerow(["client","cohort","value"])
    else:
        if client != row[0]:
            client = row[0]
            if cohort == -1 or cohort == m-1:
                cohort = 0
            else:
                cohort += 1
        newrow=[row[0],cohort,row[1]]
        writer.writerow(newrow)

    rownum += 1

ifile.close()
