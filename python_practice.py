# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

#Name: [Iliya Somov]

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
Input "N" as an integer
Set a=0 #first number
Set b=1 #second number
Set count=0
Set total=0
While count<N #This creates the cycle
    Add a to total
    Set follow_up = a+b
    Set a=b
    Set b=follow_up
    Increment count by 1
Output total
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # counts how many fibonacci numbers have been added
total = 0 # sum of the fibonacci numbers up to "N"

while count < N:
    #adds the current fibonacci number "a" to the total
    total = total + a #error was here, swapped b to a

    #Computes the next Fibonacci number in the sequence "b"
    next_value = a + b
    a = b
    b = next_value

    #Increments the counter
    count = count + 1

#Prints the total sum of up to "N" fibonacci numbers
print(total)

# %% ###########################################################
# Problem 3: Using common Python libraries
import numpy as np 

fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # first 10 numbers in fib sequence
std_fib_numbers = np.std(fib_numbers) # calculates standard deviation and saves it
print(std_fib_numbers) #prints std of fib numbers
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.
def fib_sum(N):
    a,b=0,1 #first two fibonacci numbers
    total = 0
    count = 0
    while count < N: #similar to problem 2 cycle, moves up the chain of fibonacci
        total += a
        a,b = b, a+b
        count +=1
    return total #returns sum

numbers = [5, 10, 15, 20, 25, 30] #numbers given
sums = [fib_sum(n) for n in numbers] #creates a list of sums for the different numbers given
print(sums) #shows results


# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #ERROR WAS HERE: was "0" as a string, should be an integer (TypeError)
    b = 1 #ERROR WAS HERE: was "1" as a string, should be an integer (TypeError)
    index=0 #ERROR WAS HERE: index was not defined (NameError)

    while a <= limit: ##Thrown Errors here because a and b were strings, source of errors above
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit): #changed name to odd, was even
    a, b = 0, 1
    total = 0
    while b <= limit:
        #Error in line below, should be 1 if wanting to add the odd numbers
        if b % 2 == 1:  # This line checks if the Fibonacci number is even
            total += b #Should have been +=, was just =
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_odd_fib(1))
print(sum_odd_fib(2))
print(sum_odd_fib(10))  
print(sum_odd_fib(20)) 
print(sum_odd_fib(50))

# %%
