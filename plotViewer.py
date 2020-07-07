# Name = Monish Manjunath
# Date = 03/01/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = "https://youtu.be/xxX67kXHjsw"


import random

class SimplePlotGenerator():
    """ This class reads the files and also acts as the base class for all the other plot generator class """

    def __init__(self, output = "Something Happens"):
        """ This is the constructor which prints the appropriate output when called """
        self.output = output

    def generate(self):
        """  This function returns the output of the simple plot generator """
        return self.output

    def inputOutput(self, setViewer):
        """ This function is used to set the IO if the function is called through the viewer  """
        self.controllerViewer = setViewer

    def readFile(self):
        """ This function opens reads and closes the file """

        self.openPlotNamesFile  = open("/Users/mgblr77/Desktop/plot_names.txt", "r")                # Open Plot Names file
        self.plotNames = self.openPlotNamesFile.read().split("\n")                                  # Read Plot Names file
        self.openPlotNamesFile.close()                                                              # Close Plot Names file

        self.openPlotAdjectiveFile = open("/Users/mgblr77/Desktop/plot_adjectives.txt", "r")        # Open Plot Ajdective file
        self.plotAdjectives = self.openPlotAdjectiveFile.read().split("\n")                         # Read Plot Ajdective file
        self.openPlotAdjectiveFile.close()                                                          # Close Plot Ajdective file

        self.openPlotProfessionFile = open("/Users/mgblr77/Desktop/plot_profesions.txt", "r")       # Open Plot Profession file
        self.plotProfession = self.openPlotProfessionFile.read().split("\n")                        # Read Plot Profession file
        self.openPlotProfessionFile.close()                                                         # Close Plot Profession file

        self.openPlotVerbsFile = open("/Users/mgblr77/Desktop/plot_verbs.txt", "r")                 # Open Plot Verbs file
        self.plotVerbs = self.openPlotVerbsFile.read().split("\n")                                  # Read Plot Verbs file       
        self.openPlotVerbsFile.close()                                                              # Close Plot Verbs file

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
        self.readFile()                                                             # Calling the read file function 
    
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
        self.readFile()                                                       # Calling the read file function 
                                                              
        

    def queryTheView(self, lstofdata, prompt):
        """ This function selects 5 random words for each category and appends it to the list """
        self.count = 5
        selection = []                     
        for i in range(self.count):                                          # Loop for randomly choosing 5 words from the list
            data = random.choice(lstofdata)
            selection.append(data)
        return self.controllerViewer(selection,prompt)                       # Calling the controller viewer function 

       
    def controllerViewer(self,selection,prompt):
        """ This function is a standard IO and is called when the geneator class is not connected to view and controller """

        print("Displaying wihtout the viewer and the controller")
        for i in range(self.count):                                         # Loop to print the 5 selected words in the prompt
            print(i ," - ", selection[i])
        select = int(input(prompt))                                        # prompt input form the user

        if (select < 0) or (select > len(selection)):                      # If condition to check if the user entered a valid input
            print("Enter A valid input: ")
            select = int(input(prompt))

        return selection[select]


    def readInput(self):
        """ This fucntion reads the appropriate file into a list and calls the query the view  method by sending the required parameters """

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
        self.readInput()                                                        # Calling the readInput function 
        return self.sentence


class PlotViewer():
    """ This function serves as both the view and the controller for the plot generator classes """
    
    def __init__(self):
        """ This is constructor class where we intialize the count and a call function to call the input output function  """
        self.count = 5
        self.call = None

    def registerPlotGenerator(self, call):
        """ This function registors a plot generator class with the viewer and controller """
        self.call = call
        self.call.inputOutput(self.controllerViewer)                        # Calling the inputOutput function to set the viewer

    def controllerViewer(self,selection,prompt):
        """ This function is called when the generator is connected to view/controller """

        print("Displaying through the viewer and the controller")
        for i in range(self.count):                                        # Loop to print the 5 selected words in the prompt
            print(i ," - ", selection[i])
        select = int(input(prompt))                                        # prompt input form the user

        if (select < 0) or (select > len(selection)):                      # If condition to check if the user entered a valid input
            print("Enter A valid input: ")
            select = int(input(prompt))

        return selection[select]

    def generate(self):
        """ This function prints the generated sentence """

        if self.call is not None:
            print("\nThis ouptut is printed using the viewer \n")
            print("The generated sentence is :", self.call.generate(), "\n")
        else:
            print("No plot generator has been registered")
    

    
def main():
    """ This is main function which creates an object of each class and calls the generate function of each class """

    # pg = SimplePlotGenerator()
    # print(pg.generate())

    # pg = RandomPlotGenerator()
    # print(pg.generate())

    # pg = InteractivePlotGenerator()
    # print(pg.generate())

    # pv = PlotViewer()
    # pv.registerPlotGenerator(SimplePlotGenerator())
    # pv.generate()

    # pv = PlotViewer()
    # pv.registerPlotGenerator(RandomPlotGenerator())
    # pv.generate()
      
    pv = PlotViewer()
    pv.registerPlotGenerator(InteractivePlotGenerator())
    pv.generate()

    
main()
        
        


