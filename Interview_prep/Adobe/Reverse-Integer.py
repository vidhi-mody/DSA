class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x < 0):
            x = str(x)[1:]
            x = "-" + x[::-1]
            x = int(x)
            if(x < -2**31):
                return 0
            else:
                return(x)
        else:
            x = str(x)[::-1]
            x = int(x)
            if(x > 2**31 - 1):
                return 0
            else:
                return x