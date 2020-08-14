class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        for i in range(len(s)):
            if(s[i] == 'A'):
                countA = countA + 1
                if(countA > 1):
                    return False
            elif(s[i] == 'L' and i < len(s) - 2):
                if(s[i+1] and s[i+2] and s[i+1] == 'L' and s[i+2] == 'L'):
                    return False
        return True