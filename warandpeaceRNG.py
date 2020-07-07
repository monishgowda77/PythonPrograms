# Name = Monish Manjunath
# Date = 02/22/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = "https://youtu.be/60bOo0Pe-_4"

# Before executing this program uncomment the commented lines of code below


import random
from statistics import mean
import time

class WarAndPeacePseudoRandomNumberGenerator():                     
    
    def __init__(self, seedValue=0):           
        """  This is a constructor class which initialized the seed value depedning on the input  """         
        self.seed = seedValue                               #Initalising seed value to seed
        if seedValue == 0:                                  # If the seed value is not given by the user , 
            seedValue = int(time.time())                    # The seed value = to time stamp of the system
        self.openFile = 0                               
        self.readFile()                                     # Calling the read file function 
        
    def readFile(self):   
        """ Thsi function reads the text file in read mode  """                      
        if self.openFile:                                   
            self.openFile.close()                           # Closing the file 
        self.openFile = open("/Users/mgblr77/Desktop/war-and-peace.txt", "r")   # Opening the file in read mode
        self.openFile.read(self.seed)                                           # Traversing through the file for a disatnce of seed value
        
        
    def random(self):
        """ This fucntion generates the a single random number by using the list of 32 0's and 1's """

        bits = ""                                                               
        
        for i in range(32):                                  # Looping 32 times to get 32 bits (0's and 1's) to generate a random number
            self.openFile.read(self.seed)                       

            char_1 = self.openFile.read(1)                   # Reading the first character                                  
            if not char_1:                                   # Checking if the characater is not in file - it means the file is empty
                self.readFile()                              # Reading the file again
                char_1 = self.openFile.read(1)            
            self.openFile.read(self.seed)                    # Moving the read curser by seed amount of characters
            
            Char_2 = self.openFile.read(1)                   # Reading the second character 
            if not Char_2:                                   # Checking if the characater is not in file - it means the file is empty
                self.readFile()                              # Reading the file again
                Char_2 = self.openFile.read(1)            
            self.openFile.read(self.seed)
            
            if char_1 > Char_2:                             # Conditions to genrate 0's and 1's
                bits += "1"
            else:
                bits += "0"

        return int(bits,base=2)/4294967295                  # returning the 32 bits of 0's and 1's and the max number that can be genrated (number generated if all 32 biuts were 1's)



def main():
    """ This fucntion creates an object for class and calls the appropriate fucntion using the object """

    prng = WarAndPeacePseudoRandomNumberGenerator()     # Creating an object of WarAndPeacePseudoRandomNumberGenerator class 
   
    # lstofNumbers = []                                        # A list containing the random numbers  
                                                        
    # for i in range(10000):                                   # Looping and generating random numbers 
    #     val = prng.random()                            
    #     lstofNumbers.append(val)
    
    # minimum = min(lstofNumbers)
    # print("The minimum value of 10000 random numbers is :" +str(minimum) + " \n")

    # maximum = max(lstofNumbers)
    # print("The maximun value of 10000 random numbers is :" +str(maximum) + " \n")


    # meanval  = mean(lstofNumbers)
    # print("The mean value of 10000 random numbers is :" +str(meanval)+ " \n")


main()
