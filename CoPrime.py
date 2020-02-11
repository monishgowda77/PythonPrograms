# Name = Monish Manjunath
# Date = 01/11/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/sqen3DSSDJw "



def coprime(a,b):
    
     """ Compares greatest common divisor = 1 and prints the appropriate statement """

     if ( GCD(a,b) == 1):                               # Compares if the returned gcd value is equal to 1 and prints output
        print("The numbers are Co-Prime") 
     else: 
        print("The numbers are not Co-Prime")  

def GCD(a,b): 

     """ This function returns the greatest common divisor by comparing the inputs to 0, if both are equal and """
     """checks which input is greater """

 
     if (a == 0 or b == 0): return 0                    # Checks if the either of the input are equal to 0

     if (a == b): return a                              # Checks if both numbers are equal
      
     if (a > b):                                        # Compares both the number to see which is greater 
          return GCD(a - b, b)                          # if (a > b) this line is executed
              
     return GCD(a, b - a)                               # if (b > a) this line is executed


def coprime_test_loop():

     """ Collects the two inputs from the users and calls the coprime function for evaluation """

     a = eval(input('enter 1st numbers: '))
     b = eval(input('enter 2nd numbers: '))

     coprime(a,b)                                      # Calling coprime function
                                                
     x= input('do you want to continue(y or n): ')     # Checking if the user wants to continue or quit
     if x == 'y':
          coprime_test_loop()
     if x =='n':
          return

coprime_test_loop()                                    # Calling coprime_test_loop function








