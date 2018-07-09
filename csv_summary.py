#!/usr/bin/env python2

"""Creates a CSV file to compare estimated and real results.
Input: dataset.csv, recovered.csv
Output: comparison.csv (stdout)
"""

import csv
import sys

if len(sys.argv) != 3:
    print ("Usage: csv_summary.py dataset.csv recovered.csv > comparison.csv")
    sys.exit(1)

dataset = sys.argv[1]
results = sys.argv[2]


ifile = open(results, "rb")
readerResults = csv.reader(ifile)
dictionary = dict()
rownum = 0

for row in readerResults:
    if rownum != 0:
        stringValue = row[0].strip('"')
        estimate = int(row[1])
        dictionary[stringValue] = [0,estimate]
    rownum +=1

ifile.close()

ifile = open(dataset, "rb")
readerDataset = csv.reader(ifile)
rownum = 0

for row in readerDataset:
    if rownum != 0:
        stringValue = row[1]
        if stringValue in dictionary:
            dictionary[stringValue][0] += 1
        else:
            dictionary[stringValue] = [1,0]
    rownum +=1

ifile.close()

writer = csv.writer(sys.stdout)
writer.writerow(["value","real","estimate"])
for item in dictionary:
    writer.writerow([item,dictionary[item][0],dictionary[item][1]])

exit(0)
