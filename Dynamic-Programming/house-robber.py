class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = [0 for i in range(len(nums)+1)]
        if not nums: 
            return 0
        if len(nums) <= 2: 
            return max(nums)
        if len(nums) == 3: 
            return max(nums[1], nums[0]+nums[2])
        answer[0] = 0
        answer[1] = nums[0]
        for i in range(2, len(answer)):
            answer[i] = max(answer[i-2]+nums[i-1], answer[i-1])
        return answer[len(answer)-1]