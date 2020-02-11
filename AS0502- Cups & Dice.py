# Name = Monish Manjunath
# Date = 02/09/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/F8pEll_Y6Ao "


from numpy.random import randint

class NSidedDie:
    """ This is a generic die class. the parent class of all the die classes"""
    n = 0                               
    x = 0

    def roll(self):
        """This function rolls the dice and generates a value using random nummber generator  """
        self.x = randint(1, self.n+1)                                        # Exclusive of the upper bound
        return self.x   

    def getFaceValue(self):
        """ This function is called when you want to get the face value of rolled die"""
        return self.x

    def __repr__(self):
        """ This function returns the cannonical string representation of Die object """
        return ('SixSidedDie ({})'.format(self.x))


class SixSidedDie(NSidedDie):
    """  This class inherits all the methods of Genric Die class and the no of sides for a die here is 6"""

    def __init__(self):
        self.n = 6
    

class TenSidedDie(NSidedDie):
    """  This class inherits all the methods of Genric Die class and the no of sides for a die here is 10"""

    def __init__(self):
        self.n = 10


class TwentySidedDie(NSidedDie):
    """  This class inherits all the methods of Genric Die class and the no of sides for a die here is 20"""

    def __init__(self):
        self.n = 20


class Cup:
    """ This is a cup class which composes the die classes"""
    sixSidedDiceCount = 1                                   
    tenSidedDiceCount = 1
    twentySidedDiceCount = 1
    totalValue = 0
                    
   
    diceToRollValuesList = {"SixSidedDie": [], "TenSidedDie": [], "TwentySidedDie": []}        # A property of data type Dictionary {<string, list<integers>>}  that holds the name of the dice type and all its rolled out values


    def __init__(self, sixSidedCountInputValue=1, tenSidedCountInputValue=1, twentySidedCountInputValue=1):
        """ A consturctor class used for initaiting the values"""

        self.sixSidedDiceCount = sixSidedCountInputValue
        self.tenSidedDiceCount =  tenSidedCountInputValue
        self.twentySidedDiceCount = twentySidedCountInputValue
    
    def roll(self):
        """ This function calls the roll method of each die and aggregates the total value of the dice """
        sixSidedDiceObject = SixSidedDie()                          # Creating a object of SixSidedDie class
        tenSidedDiceObject = TenSidedDie()                          # Creating a object of TenSidedDie class
        twentySidedDiceObject = TwentySidedDie()                    # Creating a object of TwentySidedDie class

        for i in range(self.sixSidedDiceCount):
            self.rollOutcome = sixSidedDiceObject.roll()
            self.totalValue += self.rollOutcome
            self.diceToRollValuesList.get("SixSidedDie").append(self.rollOutcome)

        for i in range(self.tenSidedDiceCount):
            self.rollOutcome = tenSidedDiceObject.roll()
            self.totalValue += self.rollOutcome
            self.diceToRollValuesList.get("TenSidedDie").append(self.rollOutcome)
            

        for i in range(self.twentySidedDiceCount):
            self.rollOutcome = twentySidedDiceObject.roll()
            self.totalValue += self.rollOutcome
            self.diceToRollValuesList.get("TwentySidedDie").append(self.rollOutcome)
    

    def getSum(self):
        """ This function returns the sum of all the rolled dice"""
        return self.totalValue

      
    def __repr__(self):
        """ This function prints the canonical string reprsentation of the Cup object """
        
        variableSDtringResult = ''
        for item in self.diceToRollValuesList:
            for ele in self.diceToRollValuesList[item]:
                variableSDtringResult += item + "(" + str(ele) + "),"
        
        returnValue = "Cup(" + variableSDtringResult + ")"
        return returnValue[:-2] + ")"




def main():
    """ This function asks the users for appropriate input values to play the Cups and Dice game and prints the result depending on the game result """ 
    
    print("Heyyyyy... Welcome to CUPS and DICE Game")
    userName = input("Please enter your name to continue(Name can be alpha numberic): ")
    
    if userName.isalnum():                                                              # Checking if the user has entered a name 
        balance = 100                                                                   # Assigning a balance of 100$ to the user
        print("You have a balance of 100$ ")
        userInputValue = input("Would you like to play the game? Enter yes to continue or no to exit: ")    # Askig the user of he wishes to play the game or not

        while userInputValue == "yes":
            goal =  randint(1, 101)    
            print("The goal value is " + str(goal))                                                 # Generating a random number with range 0 to 100 and assigning it as Goal value
            betPlaced =  eval(input("How much money do you want to bet: "))
            if betPlaced > 0:                                                           # Checking if the user entered valid positive bet value
                if betPlaced > balance:                                                 # Checking if the user entered a value greater than his/her balance
                    print("Sorry...You do not have enough balance to place this bet!!")
                else:
                    balance = balance - betPlaced
                    print("Enter the number of dice: ")
                    
                    six = int(input("how many of the six sided die do you want to roll: "))
                    ten = int(input("how many of the ten sided die do you want to roll: "))
                    twenty = int(input("how many of the twenty sided die do you want to roll: "))
                    
                    cup = Cup(six, ten, twenty)                                                  # Creating a object of a Cup class
                    cup.roll()                                                                   # Calling cup roll method
                    rollValue = cup.getSum()  
                    print("The roll value is " + str(rollValue))                                 # Calling get sum method of cup
                    
                    if goal == rollValue:   
                        balance += betPlaced * 10
                        print("Your goal and the value are equal, you won"+ str(betPlaced * 10) + "......" + userName + " your new balance is " + str(balance))
                    elif (rollValue <= goal + 3 and rollValue  >= goal - 3):
                        balance += betPlaced * 5
                        print("The difference between goal and value is equal or less than 3, you won "+ str(betPlaced * 5) + "...... "+ userName +  " your new balance is " + str(balance))
                    elif (rollValue <= goal + 10 and rollValue  >= goal - 10):
                        balance += betPlaced * 2
                        print("The difference between goal and value is equal or less than 10, you won "+ str(betPlaced * 2) + " ......" + userName + " your new balance is " + str(balance))
                    else:
                        print("You lost!! " + userName + "!! Your balance is: " +  str(balance))
            else:
                print("Fool!! Enter a positive number")

            userInputValue = input("press yes to continue, any other key to exit: ")    # Asking the user if he wishes to continue playing or not
            if (userInputValue != "yes"):   
                break

                        

main()
    