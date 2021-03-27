# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs.

def findStep(n) :
    if(n < 0):
        return 'Invalid Input'
    elif (n == 1 or n == 0) :
        return 1
    elif (n == 2) :
        return 2
     
    else :
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)
 
 
# Driver code
n = 4
print(findStep(n))