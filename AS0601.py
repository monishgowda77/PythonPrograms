# Name = Monish Manjunath
# Date = 02/17/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/6ND3lyFZ09M "

import statistics
from statistics import mean, median, stdev
from math import sqrt

def read():
    """ Reading the file line by line """

    fileloc = "/Users/mgblr77/Desktop/avocado.csv"
    
    infile = open(fileloc, 'r')                 # reading file in read mode
    
    volumelst = []                              # creating a list to store all the values of volume column from the data list
    lines = infile.readlines()
    i = 0
    for line in lines:                          # looping through the lines evading the heading i.e., line 1
        if i==0:
            i+=1
            continue

        line = line.split(",")
        totalVol = line[3]
        volumelst.append(float(totalVol))

    infile.close()                              # Closing the file to avoid data leakage
    return volumelst


#### 1) 

def meanFromStats():
    """Finding the mean from stats module """
    volList = read()
    
    meanValue = mean(volList)                           # Calling the mean function from module
    print("Mean value derived from stat module :" +str(meanValue)+ "\n")

meanFromStats() 

#### 2)

def stdDevFromStats():
    """ Finding the stadard deviation from stats module """

    volList = read()

    stdDevValue = stdev(volList)                         # Calling the standard deviation function from module
    print("Standard Deviation value from stat module :" + str(stdDevValue)+ "\n")

stdDevFromStats()


#### 3) 

def medianFromStats():
    """ Finding the median from stats module """

    volList = read()

    medianValue = median(volList)                        # Calling the median function from module
    print("Median value from stat module :" +str(medianValue)+ "\n")

medianFromStats()



#### 4)

def homeGrownMean():
    """ Finding the mean from homegrown code """

    volList = read()
    N = len(volList)                                # calculation the length of volume list
    sum = 0.0

    for i in volList:
            sum = sum + i

    mean = (sum/N)

    print("Mean value derievd from homegrown code: " + str(mean)+ "\n")

homeGrownMean()


#### 5) 

def homegrownSD():
    """ Finding the Standard deviation from homegrown code """
    volList = read()
    N = len(volList)                                # calculation the length of volume list

    def computeSD():
        meanValue = computeMean()                   # calling mean function 
        deviation = 0.0
        for i in volList:
            diff = (i - meanValue)
            deviation = deviation + (diff**2)
        print("Standard Deviation value derievd from homegrown code: " + str(sqrt(deviation/(N-1))) + "\n")

        
    def computeMean():                              # seperate mean fucntion returning mean vakue to homegrownSD function 
        sum = 0.0
        for i in volList:
            sum = sum + i
        return (sum/N)
    computeSD()
    

homegrownSD()



#### 6) 

def homeGrownMedian():
    """ Finding the Median from homegrown code """
    
    volList = read()
    volList = sorted(volList)
    N = len(volList)
    medianValue =  0.0
    if N%2 == 0:                                               # If th length of list is even 
        print("Median is: " + volList[N//2])
    else:                                                      # If the length of list is odd
        medianValue =  (volList[N//2] + volList[((N//2)-1)])/2
        print( "Median value derievd from homegrown code: " +str(medianValue) + "\n")
       
homeGrownMedian()


## 7) Mean from memory in a single line


def memorylessMean():
    """ This function calculates the mean value using a single line of memory """

    fileloc = "/Users/mgblr77/Desktop/avocado.csv"
   
    infile = open(fileloc, 'r')         
    i=0
    sumTotal= 0.0 
    count = 0   
    while(infile.readable()):                               # Skipping the header of the file
        if(i==0):           
            infile.readline()
            i+=1
            continue
        
        lineString = infile.readline()                       # Reading the data one line ata time
        if(len(lineString.split(",")) >= 3):            
            sumTotal = sumTotal + (float(lineString.split(",")[3]))
            count += 1
        else:                                                 # Taking care of empty lines in the dataset if any
            break                           
    return (sumTotal/count)
    


# 8) Standard devation from memory in single line


def memorylessSD(colname):
    """ This function calculates the standard deviation value using a single line of memory """

    readFile = open('/Users/mgblr77/Desktop/avocado.csv', 'r')
    row = readFile.readline()
    colnames = row.strip().split(',')           
    idx = colnames.index(colname)                   # Finding the index of the column passed

    row = readFile.readline()
    SSE = 0
    n = 0
    mean = memorylessMean()
    while row:
        SSE += (eval(row.strip().split(',')[idx]) - mean)**2
        n += 1
        row = readFile.readline()

    return (sqrt(SSE/(n-1)))



def main():

    MMmean = memorylessMean()                        # Calling memory less mean function
    MMSD  =memorylessSD('Total Volume')              # Calling memory less Standard devaition function

    print("Mean value derieved from single line memory : " +str(MMmean) + "\n")
    print("Standard Devaition value derieved from single line memory: " + str(MMSD)+ "\n")

main()





#### 9) memoryless median


# import numpy as np

# def median_approx(value):

#     mean = memorylessMean()                          # Calling mean function
#     std = memorylessSD("Total Volume")               # Calling standard deviation function

#     B = 10                                    # Creating 10 bins to hold the data
#     
#     low = 1000000000                          # Creating counters high, low, toolow and toohigh
#     high = 0
#     n = 0
#     tooLow = 0
#     tooHigh =  0                              
#     left_bin = 0
#     bins = np.zeros(B)
#     bin_width = 2*std/B
#     count = 0
#     
#     while row:
#         val = eval(row.strip().split(',')[3])         #splitting the row and taking only the total volume value

#         low = min(val, low)                           # Traversing through the list of numbers and finding min, max and n values
#         high = max(val, high)
#         n += 1
#         row = fileRead.readline()

#     range = (high - low)/10
    
#     while True:
#         count += 1
#         if float(value) < mean - std:    
#             left_bin += 1
#         elif float(value) < mean + std:
#             bin = int((float(value) - (mean - std))/bin_width)
#             bins[bin] += 1
            
#     N = len(count)
#     mid = (N + 1)/2

#     count = left_bin
#     for b, bincount in enumerate(bins):
#         count += bincount
#         if count >= mid:
#             # Stop when the count exceeds the midpoint
#             break
#     #print(b)
#     width = 2*std/B
#     median = mean - std + width*(b + 0.5)
#     print (median)



# def memeorylessMedian(colname):
#     readFile = open('/Users/mgblr77/Desktop/avocado.csv', 'r')
#     row = readFile.readline()
#     colnames = row.strip().split(',')
#     idx = colnames.index(colname)
    
#     n = 0
#     while row:
#         n += 1
#         row = readFile.readline().strip().split(',')[idx]
#         # row = readFile.readline()
#         median_approx(row)


# memeorylessMedian("Total Volume")