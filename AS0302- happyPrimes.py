# Name = Monish Manjunath
# Date = 01/26/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/Pi0myqXDfBc "


from math import sqrt, ceil                             # importing square root and ceiling inbuilt fucntion from math library


def checkPrime(x):
    """ This function checks if a number is prime or not and returns a boolean expression """
   
    y = ceil(sqrt(x))                           # finding the square root of the value to reduce the number of divisor value 
    
    for num in range(y, 1, -1):                 
        if(x % num == 0):                       
            return False                        # returen false if the modulus is zero for any number

    return True                                 # returns true for prime numbers




product = []                                     # Creating a list to store all the numbers after splitting to check for recursion in sad numbers

def isHappyNumber(a):
    """ This function checks if the sum ends with 1 for happy numbers and checks the list if the number is repeated for sad numbers  """

    p = getSquareProduct(a)                       # Calling get square product function     
    if(p == 1):                                   # Checks if the number = 1
        return (1, p)
    if(p in product):                             # Checks if the number is present in the list
        return (0, p)
    if (p not in product):
        product.append(p)                         # Appending the number to the list if it is not present in it
        return (-1, p)
    
    

def getSquareProduct(x):       
    """ this fucntion splits the number, squares it and adds the number until its 0 to get the squared value  """     

    res  = 0
    while (x != 0):
        res += int((x % 10) ** 2)                 # Adding the squared number to result
        x = int(x / 10)                           
    return res


def main():
    """ Accepts the input from the user and calls the appropriate functions to check if its happy/sad and prime/not prime number  """

while True:
    inputNumber = input(' Enter the number you want to test : ')

    happyOutput, currentProductOutput = isHappyNumber(int(inputNumber))             # Calling the is happy number function

    while(happyOutput == -1):
        if(happyOutput == -1):
            happyOutput, currentProductOutput = isHappyNumber(currentProductOutput)  # Calling the is happy number if iteration nees to continue
    
    isPrime = checkPrime(int(inputNumber))                              # Checking if the number is prime or not-prime

    if(happyOutput == 1):
        print("This is Happy and Prime number" if(isPrime) else "This is Happy and Non-Prime number")

    if(happyOutput == 0):
        print('This is Sad and Prime number' if(isPrime) else "This is sad and Non-Prime number")

    a = input("press yes to continue, any other key to exit: ")
    if (a != "yes"):
        break

main()