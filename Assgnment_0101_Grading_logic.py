# Name: Vismay Bhavinkumar Patel
# Date: 06/16/20
# Honor Statement = "I have not given or received any unauthorized assistance on this assignment"
# Video link:https://youtu.be/ViJNQFCv7ic

# Python program to perform grading logic.


print("Welcome to Grading logic Program: Proceed with the evaluation \n")


def initial():
# This function checks the initial requirements of a program like pyfile, honor statement, name, date and video_link, if they are not present marks = 0

    lst = ['pyfile','name_date','line','link']              # We will initialize all the required initials in the list

    for i in lst:
    # This loop check if the requirements in the list are fullfilled, If yes another question will be asked. Otherwies marks will be zero
     

        pyfile = input( " Is there a .py file in the assignment submission? (Yes/No) \n " )    # User input to check the condition whether .py is present or not.

        if ( pyfile == 'No'):           # check if pyfile is available.
            print( "marks: 0" )           # If .py file is not available marks = 0.
            return 0                    # 'return 0' will terminate the current loop and exit the function, terminating the programme.   
            
            
        name_date = input( " Is there a name and date mentioned in the file? (Yes/No) \n" )    # User input to check if name is present or not. 
        
        if ( name_date == 'No'):        # check if name and date are mentioned in the programme file. 
            print( "marks: 0" )           # If name and date are absent marks = 0.
            return 0                    # 'return 0' terminates the current loop and exits the function, terminating the programme. 
          

        line = input( " Is there a honor statement? (Yes/No) \n" )      # User input to check if the honor statement was mentioned, to avoid plagerism. 
        
        if ( line == 'No' ):            # checks the honor statement.
            print( "marks: 0" )           # 0 marks are avorded if honor statement is not present in the file. 
            return 0                    # return statement exits the loop and programme, from further execution. 
         

        link = input( " Is there a youtube link? (Yes/No) \n" )     # User input to check if the youtube link is attached in the .py file.  

        if ( link == 'No' ):            # checks the youtube link.
            print( "marks: 0" )           # If youtube link is not present, 0 marks are given. 
            return 0                    # return statement exits the loop and programme.
        


        def scores( correctness, elegence, hygine, video, late ):
        # This function is used to calculate the total score and input scores for correctness, elegence, hygene, video and late assignment in code.  

           total = correctness + elegence + hygine + video          # Calculating the total score after asking values from user.

           if ( late == 'Yes' ):
           # This if condition evaluates whether the assignment was late.
              
               hours_late = int( input( "How late the assignment was submitted?? (in hours) \n" ) )   # User is asked, how many hours the assignment was late.
               
               total_late = total - 0.01*hours_late                          # Calculation for the deduction in total base on 1% marks per hour.
               print( "Total score achieved after late submission:" )        # Prints the STATEMENT total marks after late submission.
               return total_late                                             # RETURNS the total_late score. 
           
           else:
           # If the assignment was not late, total value is returned, here in else condition.

               print( "Total score achieved: " ) 
               return total 
 
       
        # Series of integer input statements, which ask for the marks of the students based on the following criteria.
         
        correct_score = int (input ( "Enter the marks for correctness of the code, out of 10: \n" ))
        elegence_score = int (input ( "Enter the marks based on elegence of the code, out of 10: \n" ))
        hygine_score = int (input ( "Enter the marks based on hygene, out of 10: \n" ))
        video_score = int (input ( "Enter the marks out of 10, based on youtube discussion: \n" ))
        late_score = input ( "Did the student do late submission? (Yes/No) \n" )

        print(scores( correct_score, elegence_score, hygine_score, video_score, late_score ))   # Defining the function parameters. 

        break    # Breaks the loop when the program is executed successfully, and avoids repetation of the first line.

initial()