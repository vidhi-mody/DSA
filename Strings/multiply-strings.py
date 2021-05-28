# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2
# also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0':0
        }
        m = len(num1)
        n = len(num2)
        int_num1 = 0
        int_num2= 0
        for i in range(m):
            int_num1 = int_num1 * 10 + nums[num1[i]]
        
        for i in range(n):
            int_num2 = int_num2 * 10 + nums[num2[i]]
        
        return str(int_num1*int_num2)