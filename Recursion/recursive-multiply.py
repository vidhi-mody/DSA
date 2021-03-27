#Write a recursive function to multiply two positive integers without using the *operator.
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

def multiply(num1, num2):
    if(num2 == 0):
        return 0
    # Add num1 one by one
    if(num2 > 0 ):
        return (num1 + multiply(num1, num2 - 1))
 
    # The case where num2 is negative
    if(num2 < 0 ):
        return -multiply(num1, -num2)
    
# Driver code
num1 = 10
num2 = 24
print(multiply(num1, num2))