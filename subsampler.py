#!/usr/bin/python

"""Creates a subsample of the dataset, allowing to choose amount of users and reports per user.
Input: nusers, nreps, dataset.csv
Output: trimmed_dataset.csv (stdout) 
"""

import csv
import sys
import linecache
import random 

def indexUsers(reader):
    """Returns an index of users and the minimum amount of reports per user"""
    rowNum = 0
    minReps=sys.maxint
    tmpMinReps=sys.maxint
    client = ""
    listClients = []
    listIterator = -1
    firstRow = []
    for row in reader:
        if rowNum != 0:
            if client != row[0]:
                client = row[0]
                listClients.append(rowNum+1)

                if tmpMinReps < minReps:
                    minReps = tmpMinReps
                tmpMinReps = 1
           
            else:
                tmpMinReps += 1

        else:
            firstRow=row

        rowNum += 1

    return listClients, minReps, firstRow

if len(sys.argv) != 4:
    print ("Usage: dataset_trimmer.py nusers nreps dataset.csv")
    sys.exit(1)

inputNumUsers = int(sys.argv[1])
inputNumReps = int(sys.argv[2])
filename = sys.argv[3]

ifile = open(filename, "rb")
reader = csv.reader(ifile)

listUsers, minReps, firstRow = indexUsers(reader)

ifile.close()

writer = csv.writer(sys.stdout)


if  len(listUsers) < inputNumUsers:
    print "Insufficient amount of users"
    exit(1)

if minReps < inputNumReps:
    print "Insufficient minimum amount of reports per user"
    exit(1)

writer.writerow(firstRow)
for i in range(inputNumUsers):
    userPosition = listUsers.pop(random.randint(0,len(listUsers)-1))
    listOfReports =[]
    for j in range(minReps):
        listOfReports.append(linecache.getline(filename, userPosition+j).rstrip().split(','))


    for j in range(inputNumReps):
        writer.writerow(
            listOfReports.pop(
                random.randint(
                    0,len(listOfReports)-1
                    )
                )
            )
        
exit(0)
