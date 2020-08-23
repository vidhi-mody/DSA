class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest = minDiff = 10000
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while(j < k):
                current = nums[i]+nums[j]+nums[k]

                if(abs(target-current) < minDiff):
                    minDiff = abs(target-current)
                    closest = current
                    
                if(minDiff == 0):
                    return current

                if(current < target):
                    j += 1
                else:
                    k -= 1
                    
        return closest