#!/usr/bin/env python
import sys,math


if len(sys.argv) != 5:
    print ("Usage: epsilon.py f h p q")
    sys.exit(1)

f = float(sys.argv[1])
h = int(sys.argv[2])
p = float(sys.argv[3])
q = float(sys.argv[4])

eInf=2*h*math.log((1-f/2)/(f/2))

qStar=(f/2)*(p+q)+(1-f)*q
pStar=(f/2)*(p+q)+(1-f)*p

eOne=h*math.log((qStar*(1-pStar))/(pStar*(1-qStar)))
print ("ln(3) = ", math.log(3))

print ("eInf = ", eInf)
print ("eOne = ", eOne)
