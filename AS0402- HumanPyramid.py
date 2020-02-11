# Name = Monish Manjunath
# Date = 02/02/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/iw5ECj0BHx8 "

def humanPyramid(row, col):
    """ This fuction calls itself recursively to calculate the weight on a person's back  """
    if(row < col or row < 0 or col < 0):                                # If weight row value is less than column value, row or column value is negative then the value is 0
        return 0
    if(row == 0 and col == 0):                                          # This is a base case where the first person i.r., (0,0) returns only his weight
        return 128
    return  128 + humanPyramid( row - 1 , col - 1) // 2 + humanPyramid(row - 1 , col) // 2  # Calling the Human Pyramid fucntion recursively


def main():
    """ This fucntion accepts input from the user and prints the output """
    row = int(input("Enter the Row number: "))          
    col = int(input("Enter the Col number: "))

    value = humanPyramid(row,col)                                           # Calling the human pyramid function
    print ("The weight  is : " +  str(value))

main()

