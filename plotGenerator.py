# Name = Monish Manjunath
# Date = 02/29/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = "https://youtu.be/_xHhxOnoLCc"


import random

class SimplePlotGenerator():
    """ This class reads the files and also acts as the base class for all the other plot generator class """

    def __init__(self, output = "Something Happens"):
        """ This is the constructor which prints the appropriate output when called """
        self.output = output

    def generate(self):
        """  This function returns the output of the simple plot generator """
        return self.output

    def readFile(self):
        """ This function opens reads and closes the file """

        self.openPlotNamesFile  = open("/Users/mgblr77/Desktop/plot_names.txt", "r")                     # Open Plot Names file
        self.plotNames = self.openPlotNamesFile.read().split("\n")                                       # Read Plot Names file
        self.openPlotNamesFile.close()                                                                   # Close Plot Names file

        self.openPlotAdjectiveFile = open("/Users/mgblr77/Desktop/plot_adjectives.txt", "r")             # Open Plot Ajdective file
        self.plotAdjectives = self.openPlotAdjectiveFile.read().split("\n")                              # Read Plot Ajdective file
        self.openPlotAdjectiveFile.close()                                                               # Close Plot Ajdective file

        self.openPlotProfessionFile = open("/Users/mgblr77/Desktop/plot_profesions.txt", "r")            # Open Plot Profession file
        self.plotProfession = self.openPlotProfessionFile.read().split("\n")                             # Read Plot Profession file
        self.openPlotProfessionFile.close()                                                              # Close Plot Profession file

        self.openPlotVerbsFile = open("/Users/mgblr77/Desktop/plot_verbs.txt", "r")                      # Open Plot Verbs file
        self.plotVerbs = self.openPlotVerbsFile.read().split("\n")                                       # Read Plot Verbs file       
        self.openPlotVerbsFile.close()                                                                   # Close Plot Verbs file

        self.openPlotAdjectiveEvilFile = open("/Users/mgblr77/Desktop/plot_adjectives_evil.txt", "r")    # Open Plot Adjective Evil file
        self.plotAdjectiveEvil = self.openPlotAdjectiveEvilFile.read().split("\n")                       # Read Plot Adjective Evil file  
        self.openPlotAdjectiveEvilFile.close()                                                           # Close Plot Adjective Evil file

        self.openPlotVillianJobFile = open("/Users/mgblr77/Desktop/plot_villian_job.txt", "r")           # Open Plot Villian Job file
        self.plotVillianJob = self.openPlotVillianJobFile.read().split("\n")                             # Read Plot Villian Job file  
        self.openPlotVillianJobFile.close()                                                              # Close Plot Villian Job  file

        self.openPlotVillians = open("/Users/mgblr77/Desktop/plot_villains.txt", "r")                   # Open Plot Villian file
        self.plotvillians = self.openPlotVillians.read().split("\n")                                    # Read Plot Villian file
        self.openPlotVillians.close()                                                                   # Close Plot Villian file


       
class RandomPlotGenerator(SimplePlotGenerator):
    """ This class extends the simple plot generator class, reads each word in random and prints the sentence  """

    def __init__(self):
        self.readFile()                                                                 # Calling the read file function 
    
    def generate(self):
        """ This function generates a random choice of words and prints the sentence """
        name = random.choice(self.plotNames)                                            # Randomly picking a name 
        adjective = random.choice(self.plotAdjectives)                                  # Randomly picking an adjective
        profession = random.choice(self.plotProfession)                                 # Randomly picking a profession
        verb = random.choice(self.plotVerbs)                                            # Randomly picking a verb
        adjectiveEvil = random.choice(self.plotAdjectiveEvil)                           # Randomly picking an adjective evil 
        villianJob = random.choice(self.plotVillianJob)                                 # Randomly picking a villian job
        villian = random.choice(self.plotvillians)                                      # Randomly picking a villian 

        sentence = name +", a " + adjective + " " + profession+ ", must " + verb + " the " + adjectiveEvil+ " " + villianJob + ", " + villian + "."

        return sentence
    

class InteractivePlotGenerator(SimplePlotGenerator):
    """ This class inherits the simple plot generator class, it allows the user to select a word from a list of 5 randomly picked words from each category """

    def __init__(self):
        """ This is a constructor function which calls the readfile and the readInput function """
        self.readFile()                                                         # Calling the read file function 
        self.readInput()                                                        # Calling the read input function 
        

    def queryTheView(self, lstofdata, prompt):
        """ This function selects 5 random words for each category and allows the user to prompt the selected word from the list """
        count = 5
        self.selection = []                     
        for i in range(count):                                                  # Loop for randomly choosing 5 words from the list
            data = random.choice(lstofdata)
            self.selection.append(data)

        for i in range(count):                                                  # Loop to print the 5 selected words in the prompt
            print(i ," - ", self.selection[i])
        self.select = int(input(prompt))                                        # prompt input form the user

        if (self.select < 0) or (self.select > len(self.selection)):            # If condition to check if the user entered a valid input
            print("Enter A valid input: ")
            self.select = int(input(prompt))

        return self.selection[self.select]

    def readInput(self):
        """ this fucntion reads the appropriate file into a list and calls the query the view  method by sending the required parameters """

        names = self.queryTheView(self.plotNames, "Choose a Name: ")
        adjective = self.queryTheView(self.plotAdjectives, "Choose an Adjective: ")
        profession = self.queryTheView(self.plotProfession, "Choose a Profession: ")
        verb = self.queryTheView(self.plotVerbs, "Choose a verb: ")
        adjectiveEvil = self.queryTheView(self.plotAdjectiveEvil, "Choosen an Adjective Evil: ")
        villianJob = self.queryTheView(self.plotVillianJob, "Choose a villian Job: ")
        villian = self.queryTheView(self.plotvillians, "Choose a villian name: ")

        self.sentence = names +", a " + adjective + " " + profession+ ", must " + verb + " the " + adjectiveEvil+ " " + villianJob + ", " + villian + "."
        return self.sentence                                                    # Returns the sentence which has to be displayed 

    def generate(self):
        """ This fucntion returns the sentenced formed using the user selection """
        return self.sentence


def main():
    """ Main function creates an object of each class and calls the appropriate function """

    # pg = SimplePlotGenerator()                                                # Creating an object for Simple plot generator
    # print(pg.generate())

    # pg = RandomPlotGenerator()                                                # Creating an object for Random plot generator
    # print(pg.generate())

    pg = InteractivePlotGenerator()                                             # Creating an object for Interactive plot generator
    print(pg.generate())  


main()