# Name = Monish Manjunath
# Date = 02/01/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/Ws1KkL8w6zs  "


from numpy.random import seed                                  # Importig seed from numpy.random for inputing values to generate random numbers
from numpy.random import randint                               # Importing randInt from numpy. random to generate random numbers


def solveGoldbachDeuce(lst, n):

    """ This function checks the list for the two integers which sums to the value n """
    
    for num in lst:
        
        value = abs(n - num)                                    # value = the remaining value after subtracting n with first value of the list
        low = lst[0] + 1
        high = len(lst) - 1

        while low <= high:                                      # Binary search to find if the remaining value exists in the list
            mid = (low + high) // 2
            item = lst[mid] 
            if(value == item):
                print("Golbach deuce -->" + str(n) + " = " + str(num) + " + " + str(item))
                return -1
            elif (value < item):                               # If value is less than the Item
                high = mid - 1                                 # Make high as mid -1 because the value exists in the left side of the list
            else:
                low = mid + 1                                  # else make low as mid + 1 because the value exists in the right side of the list
        
    print ( "There are no two integers in the list that sum to n ")
                
                    

def main():

    """ This function accepts user inpputs and generates the list of random integers  """

    i = int(input("Enter the length of list:  "))                 # Asking the user for the length of the list for creating a list of random numbers from 0-100 
    n = int(input("Enter the N value: "))                         # Asking the user for the N value

    randNumbersLst= randint(0, 101, i )                           # Generating a list of random integers from 0 to 100 of size i 
    sortedLst  = sorted(randNumbersLst)                           # Sorting the list of random number in ascending order

    solveGoldbachDeuce(sortedLst,n)                               # Calling the solve golbach deuce function
    

main()