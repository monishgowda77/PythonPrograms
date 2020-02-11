# Name = Monish Manjunath
# Date = 01/11/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = " https://youtu.be/o_QoGiC08M0 "


def Questionaire():
    """ This function asks the user for few basic inital questions, depedning on which the grade is calculated or the grade is given as 0 """

    Filetype = input("Have you submitted the assignment as .py file? (y/n) " )
    if Filetype == 'y':                                                         # Checks if the submitted assignment is in .py format
        print('Answer the next question')
    if Filetype == 'n':
        print("Your grade is 0")
        exit()
    
    AuthName_Date = input("Does the assignment include author's name and Date? (y/n) ")
    if AuthName_Date == 'y':                                                    # Checks if the assignment contains author's name and date
        print('Answer the next question')
    if AuthName_Date == 'n':
        print("Your grade is 0")
        exit()

    Honor_Statement = input("Does the assignment include Honor statement? (y/n) ")
    if Honor_Statement == 'y':                                                  #Checks if the assignment cobtains honor statement
        print('Answer the next question')
    if Honor_Statement == 'n':
        print("Your grade is 0")
        exit()
            
    YoutubeVideolink = input("Does the assignment include a link to unlisted 3 minute youtube video? (y/n) ")
    if YoutubeVideolink == 'y':                                                 # Checks if the youtube video link is present in the assignment 
        print("All the initial conditions have been met, Proceed entering marks for the below categories")
        
        CalcScore()                                                             # Calling CalcScore (Calculate Score) method
    if YoutubeVideolink == 'n':
        print("Your grade is 0")
        exit()


def CalcScore():                                                                # Function CalcScore
    """ This function calculates the total score of the assigment depending on whether the assignment was submitted on time """

    Correctness = eval(input("Out of ten points, enter the score for correctness of code depending on the specifications met: "))
    Elegence = eval(input("Out of ten points, enter the score for the elegence of the code: "))
    Hygiene = eval(input("Out of ten points, enter the score for code hygiene: "))
    VideoQuality = eval(input("Out of ten points, enter the score based on the quality of discussion in youtube video: "))

    Total_Score = Correctness + Elegence + Hygiene + VideoQuality               # Adding all the scores 
    Late(Total_Score)                                                           # Calling late function


def Late(Total_Score):
    """ Calculates the score to be deducted from the final total score if the assignment is submitted late """

    Late_Submission = input("Was the assignment submitted late? (y/n) ")
    if Late_Submission == "y":                                                   # Checks if the assignment was submitted late or on time
        LateHours = eval(input(" Enter the number of hours late the assignment was submitted after the due time (Late assignments lose 1% per hour): "))
        LateHours_Score = LateHours/ 100 * Total_Score                      # Calculating score to be deducted from the toal score depending on the number of late hours
        Final_Score = Total_Score - LateHours_Score                         # Subtracting late hours score from total score to get the final score
        return Pstat1(Final_Score)                                          # Retrun Final score to Print function Pstat1
              
    if Late_Submission == "n":
        return Pstat2(Total_Score)                                          # Retrun Total score to Print function Pstat2
              

def Pstat1(Final_Score):
    """ Prints the assignment final score after deducting the score of delayed submission """

    print("Your Total Score is: " ,Final_Score,  "\n Good job")   


def Pstat2(Total_Score):
    """ Prints the assignment final score when the submission is in time """

    print("Your Total score is: " ,Total_Score,   "\n Good job")  


Questionaire()                                                              # Calling the Questionaire function

