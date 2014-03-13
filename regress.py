#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math

##### read the data files ########################
# I put the data in two files: 'datax.txt' and 'datay.txt'
# datay.txt contains the x values and
# datax.txt contains the y values because
# I messed up.

xfile = open("datay.txt", "r")
yfile = open("datax.txt", "r")

xvals = xfile.read()
yvals = yfile.read()

## let's strip the tab characters and replace them with spaces

xvals = xvals.replace("\t", " ")
xvals = xvals.split()
yvals = yvals.replace("\t", " ")
yvals = yvals.split()

## and finally, let's convert the numbers to floats and place them in a list
xlist = []
ylist = []
for x in xvals:
    x = float(x)
    xlist.append(x)

for y in yvals:
    y = float(y)
    ylist.append(y)




plt.plot(xlist, ylist, 'ro') ## 'ro' means draw red soycles
plt.ylabel('stuff on y')
plt.xlabel('stuff on x')
plt.show()

##### let's try to find a nice fitting curve ######

## so lets look at y = a + b*log(x) since you said the curve looks like
## a logarithmic one

xlist1 = []
ylist1 = []

for x in xlist:
    x = math.exp(x)
    xlist1.append(x)

for y in ylist:
    ylist1.append(y)


plt.plot(xlist1, ylist1, 'bo') ## blue soycles this time
plt.ylabel('more stuff on y')
plt.xlabel('more stuff on x')
plt.xlim([0,.001])
plt.show()

