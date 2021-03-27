#Write a recursive function to multiply two positive integers without using the *operator.
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

def multiply(num1, num2):
    if(num2 == 0):
        return 0
    else:
        return(num1 + multiply(num1, num2-1))
    
# Driver code
num1 = 10
num2 = 4
max1 = max(num1, num2)
min1 = min(num1,num2)
print(multiply(max1, min1))