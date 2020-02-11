# Name = Monish Manjunath
# Date = 01/25/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/OiXj5GimoJM  "


from math import sqrt, ceil                             # importing square root and ceiling inbuilt fucntion from math library

def generatePrimeNumber(mg):
    """ This function creates a list and also genrates the numbers to check if its prime or not  """

    res = [2]                                           # a list named result
    for num in range(3, mg):
        if(checkPrime(num)):                            # calling check prime function
            res.append(num)
    return res


def checkPrime(x):
    """ This function checks if a number is prime or not and returns a boolean expression """
   
    y = ceil(sqrt(x))                           # finding the square root of the value to reduce the number of divisor value 
    
    for num in range(y, 1, -1):                 
        if(x % num == 0):                       
            return False                        # returen false if the modulus is zero for any number

    return True                                 # returns true for prime numbers



def solveGoldbachConjecture(z):
    """ This fucntion finds the two prime numbers that sum to the even integer value  """

    primeNumbers = generatePrimeNumber(100)       # Calling genrate Prime number function and assigning the list of primes to the prime numbers
    for p in primeNumbers:
        if(p <= z):                               # Checking if the even number valuse is less than or equal to initial prime number 
            if(z-p in primeNumbers):              # Checkig if the diffrence value betwen prime and even number is in the list of primes
                print( "Goldbach Conjecture --> " + str(z) + " = " + str(p) + " + " + str(z-p))
                break 




def mainLoop():                     
    """ this fucntion iterates over even integers from 4 to 100 """           

    for x in range(4,100,2):                      
        solveGoldbachConjecture(x)                 # calling solve goldbach conjecture funtion


mainLoop()                                      