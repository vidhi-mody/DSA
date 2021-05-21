#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        elif(x < 10):
            return True
        else:
            number = x
            revs_number = 0
            while (number > 0):  
                remainder = number % 10  
                revs_number = (revs_number * 10) + remainder  
                number = number // 10 
            if(x == revs_number):
                return True
            else:
                return False