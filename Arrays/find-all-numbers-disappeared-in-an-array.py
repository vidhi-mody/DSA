class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        
        li=[0] * len(nums)
        for n in nums:
            li[n-1] = n  
            
        answer = []
        for i in range(len(li)):
            if li[i] == 0:
                answer.append(i+1)
        return answer