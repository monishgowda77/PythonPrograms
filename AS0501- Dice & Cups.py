# Name = Monish Manjunath
# Date = 02/08/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/hkuJ5ALPD2s "


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
        return ('Die ({})'.format(self.x))


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
    """ This a cup class which composes the die classes"""
    sixSidedDiceCount = 1                                   
    tenSidedDiceCount = 1
    twentySidedDiceCount = 1
    totalValue = 0
                    
   
    diceToRollValuesList = {"SixSidedDie": [], "TenSidedDie": [], "TwentySidedDie": []}        # A property of data type Dictionary {<string, list<integers>>} that holds the name of the dice type and all its rolled out values

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
    """ Creates an object type of the cup class and calls the appropriate functions"""

    # cup = Cup(1,1,1)
    # cup.roll()  
    # print(cup.getSum())
    # print(cup)


    # cup = Cup(2,1,2)
    # cup.roll()
    # print(cup.getSum())
    # print(cup)

    cup = Cup(10,10,10)
    cup.roll()
    print(cup.getSum())
    print(cup)


main()