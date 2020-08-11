class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        n = len(str)
        answer = ""
        for i in range(n):
            if(ord(str[i]) < 90 and ord(str[i]) > 64):
                answer = answer + chr(ord(str[i]) + 32)
            else:
                answer = answer + str[i]
        return answer