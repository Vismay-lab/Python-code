# Name: Vismay Bhavinkumar Patel    
# Date: 07/12/20
# Honor Statement: “I have not given or received any unauthorized assistance on this assignment.” 
# youtube link: https://youtu.be/5LsEErwmlNA

# Python Program on Human Pyramid with recursion

def HumanPyramid(row, column, Weight):
    """
    calculates the weights carried by the person using recursive function 
    1. If the row = 0 then the weight carried is 0 
    2. When column = 0 this checks the criteris for the person having weight of one person and standing at the end of the row.
    3. when the row and column are equal then the weight is split according to where the preson is standing. 
    4. otherwise the weight is calculated based on the position of the person. 
    """
    
    if (row == 0):                  # if the row is 0 then the weight carried is zero 
        return 0                
            
    elif column == 0:               # when the column value is zero, the weight is checked for the last person on the corner.

        return ( HumanPyramid (row-1, column, Weight) + Weight) // 2    # here we are evaluating the row value and the weight computed in the column divided by 2 
    
    elif row == column:             # when both the row and column have same position

        return ( HumanPyramid (row-1, column-1, Weight) + Weight) // 2    # here the weight is calculated based on the position of the person
                                                                          # and th weight he/she is holding above them and if someone else is 
                                                                          # carrying their weight, or they are at the bottom 

    else:                           # the weight calculated if the person is at the corner and is taking half weight of the person above him.       

        return Weight + ( HumanPyramid (row-1, column-1, Weight // 2 ) + ( HumanPyramid ( row-1, column, Weight ) // 2 ))


def main():
    
    """
    The structure of the program is defined here
    1. Enter row value 
    2. Enter column value 
    3. substitute it in the function 
    4. display the result
    """

    r = int(input("enter the row"))                     # User input for row 

    c = int(input("enter the column"))                  # User input for column

    weight = 128                                        # initializing the value of weight

    output = HumanPyramid( r, c, 128 )                  # storng the output of the function in the variable output

    print("Weight carried by the person:", output)      # printing the output

main()