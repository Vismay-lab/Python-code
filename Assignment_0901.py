# Name: Vismay Bhavinkumar Patel 
# Date: 08/12/20 
# Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”
# Youtube Link: https://youtu.be/WE2xBWNgenY

# Python programme to perform basic functions of NumPy package

import numpy as np

a = np.array([[1,2,3], [0,1,4]])
print(a.size)
"""
import numpy as np

a = np.arange(100)                        # Creating an array of 100 numbers which are equally spaced.  

print( ' \n Array a = \n\n ', a )         # Printing array a
print('\n')                               # Providing spacing after output


b = np.arange(0, 100, 10)                 # Creating an array with 10 equally spaced values from range 0-100.

print( ' \n Array b = \n\n ', b )         # Printing array b
print('\n')                               # Providing spacing


c = np.linspace(0.1, 10, 100)             # Using linespace to create an array with 0.1 spacing from range 0-10.

print( ' \n Linespace c = \n\n ', c )     # Printing linespace array c
print('\n')                               # Providing spacing 


d = np.random.rand(10,10)                 # Creating a random 2D array with 10/10 dimensions.

print( ' \n 2D Array d = \n\n', d )       # Printing 2D array.
print('\n')                               # Giving spacing.


a = np.arange(100).reshape(10,10)         # reshaping array 'a' into a 10/10 2D matrix

print( ' \n  Reshape Array a:  \n\n ', a )     # Printing reshaped array a
print('\n')                                    # Giving spaceing


print( " \n Output of a[4,5]: ", a[4,5] )      # output of position a[4,5]
print('\n')                                    # Giving space after output


print( " \n Output of a[4]: ", a[4] )          # Output of position a[4]
print('\n')                                    # Giving space after output


print(" \n Sum of d: ", d.sum())               # Summation of arrary d 
print('\n')                                    # Providing space


print(" \n Maximum of a: ", a.max() )          # Printing the maximum value in array a.
print('\n')                                    # Providing spacing after output


print( " \n Transpose of b: \n" )              # performing transpose of a array b

transpose = np.matrix(b).T                     # assigning variable transpose operation

print(transpose)                               # printing the output
print('\n')                                    # providing spacing


print( " \n Adding a and d: \n " )             # Adding a and d
print( a + d )                                 # Operation to add a and d
print('\n')                                    # Giving space after printing output


print( " \n Multiplication of a and d: \n " )  # Multiplication (Binary operation that produces a matrix by the product of the number of rows nad number of columns of two matrix) of a and d 
print( a * d )                                 # Multiplicatio operation      
print('\n')                                    # Providing spacing


print( " \n dot product of a and d \n " )      # Dot product (sum of the product of the corresponding entries of the two sequences of numbers) of a and d
print( np.dot(a,d) )                           # Displaying dot product
print('\n')                                    # Providing spacing
"""
