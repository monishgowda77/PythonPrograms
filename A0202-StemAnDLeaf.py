# Name = Monish Manjunath
# Date = 01/18/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/F_3reHZGJOI "



import os                                                         # importing the os modeule which is used below for reading the posix file path


def greetUser():
    """" This function prints a message for greeting the user and also briefly explains what the program output """
   
    print('Hi, I hope you are doing well')
    print('This is a simulation which produces a stem and leaf plot for the file number you enter')
    print('There are 3 files where there are a mix of 2,3 and 4 digit numbers in each file')
    print('Feel free to enter the file number of your choice to get a stem and leaf plot of the same')


def getFileInput():
    """ This function prompts the user to enter the file number as input and returns it """    
    
    x = input(" Choose a file number out of 1, 2 & 3 :  " )         # Recieves the user input and stores in a variable x
    return x


def readFile(FileNumber):
    """ This function accepts the file number input and reads the appropriate file using its path """   

    filePath = '~/Desktop/StemAndLeaf' + FileNumber + '.txt'        # Appends the inputted file number to the file path

    fileFinal = os.path.expanduser(filePath)
    f = open(fileFinal, "r")                                        # Opens the file in read mode
    lineList = f.readlines()
    f.close()                                                       # Closes the file 
    x = []                                                          # Declaring a list with name x

    for i in range ( 0, len(lineList) ):
        x.append(lineList[i].strip())                                                      
    return x



def displayPlot(lstNumbers):
    """ This function generates the stem and leaves from the list of numbers and prints it in a sorted order """

    sortedLst = sort(lstNumbers)                                # Calling sort function  
    stemAndLeaves = generateStemAndLeaves(sortedLst)            # Calling generate stem and leaves function 


    sortedKeys = sorted(stemAndLeaves.keys())                   # Sorting the stems i.e., the keys

    for key in sortedKeys:
        print(str(key) + '|' + ','.join(stemAndLeaves[key]))    # Printing the stems and leaves in stem and leaf plot format



def sort(lstNumbers):
    """ This functions sorts the list of numbers in ascending order """ 

    lstNumbers.sort()
    return lstNumbers 


def generateStemAndLeaves(sortedLst):
    """ This function searches for the stem in the dictionary and appends the leaves to the appropriate stems or 
        creates a new stem and appends the leaves to that stem """

    stemAndLeaves = {}                                          # Creating a dictionary with keys = stem and value = leaf pairs

    for i in range( 0, len(sortedLst) ):
        currentItem = sortedLst[i]
        [stem, leaf] = splitStemAndLeaves(currentItem)          # Calling split stem and leaf function
    
        if(stemAndLeaves.get(stem) == None):                    # Searches if the stem is im the dictinory or it needs to be added
            stemAndLeaves[stem] = [leaf]
        else:
            stemAndLeaves[stem].append(leaf)
    return stemAndLeaves
    

def splitStemAndLeaves(currentItem):
    """ This function splits each number into stem and leaves """

    if(len(currentItem) == 1):                                  # If its a single digit number assign stem as 0 and the single digit to leaf
        stem = 0        
        leaf = currentItem                                      
    else:
        stem = int(currentItem[ : -1])                       # Splitting the item into stem and leaf by slicing
        leaf =currentItem [-1: ]
    return [stem,leaf]



def steamLeafPlot():
    """ This is the main function which contains the calls for the other sub functions """
    
    while True:                                             # A while loop which executes the simulation until the user wishes to exit
        greetUser()                                         # Calling greet user function
        FileNumber = getFileInput()                         # Calling get File Input function
        lstNumbers = readFile(FileNumber)                   # Calling read file function
        displayPlot(lstNumbers)                             # Calling display plot function

        a = input("press yes to continue, any other key to exit: ")
        if (a != "yes"):
            break

steamLeafPlot()