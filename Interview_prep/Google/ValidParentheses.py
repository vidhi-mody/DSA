class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if(s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
            else:
                if(stack):
                    temp = stack[-1]
                    if(s[i] == ")"):
                        if(temp == "("):
                            stack.pop()
                        else:
                            return False
                    elif(s[i] == "}"):
                        if(temp == "{"):
                            stack.pop()
                        else:
                            return False
                    else:
                        if(temp == "["):
                            stack.pop()
                        else:
                            return False
                else:
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False
                