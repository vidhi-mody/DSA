class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return 
        self.dp=[nums[0]]
        
        for i in range(1,len(nums)):
            self.dp.append(self.dp[i-1]+nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if(i ==0 or j == 0):
            return self.dp[j]
        else:
            return self.dp[j]-self.dp[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)