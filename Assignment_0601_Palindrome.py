# Name : Vismay Bhavinkumar Patel
# Date : 07/25/20
# Honor statement : "I have not given or received any unauthorized assistance on this assignment."
# Youtube Link : https://youtu.be/CnDQZhh5ihQ

# Python program for Palindrome Dates


def check_palindrome(DATE):

    """
    This function will check if the date is palindrome or not.
    We will be using the '/' sigh to seperate the date , month and year
    If condition will evaluate if the date is palindtome.
    """
    
    DATE = DATE.replace('/', '')        # replace '/' with space between the digits, to geet DD/MM/YYYY output.

    if DATE[::-1] == DATE:              # If condition that checks the dates from last to first for being a palindrome

        return True                     # If the date is palindtome returnns true

    return False                        # Else returns false, if the date is not palindrome.



month_list = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # Making a list of number of days in a month, for 12 months


file = open('Palindrome_Dates.txt', "w")        # We have opend a file to write where the dates with plaindrome will bw stored.


for years in range(2000,2100):                  # For loop that iterates through the every year in the 21'st century.


    for months in range(1,13):           # For loop that loops through the all the days in the 12 months.


        for Day in range(1, month_list[months]+1):    # this for loop iterates through the dates in the specific format 
                                                                # represented by f strings. And evaluates if the date is palindrome or not.


            DATE = f'{Day:02}/{months:02}/{years:04}'    # Here we are using f'strings to get a proper representation of dates. 


            if check_palindrome(DATE):          # If condition calls the function declared above and checks if the date is palindrome or not.
                                                # Based on the formate given by the f'string.

                file.write(DATE)                # If the condition is true we write the palindrome dates.

                file.write("\n")                # Giving a space    


file.close()          # closing the file.




    