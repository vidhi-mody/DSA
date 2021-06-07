# Given a string s consists of some words separated by spaces, return the length of the last word in the string. 
# If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s == " "):
            return 0
        words = s.split(" ")
        n = len(words) - 1
        while(n > -1):
            if(len(words[n]) != 0):
                return len(words[n])
            else:
                n -= 1
        return 0