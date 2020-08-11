class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[i] = nums[i]
        for i in range(len(nums)):
            x = target - nums[i]
            if(x in my_dict.values() and nums.index(x) != i):
                return [i, nums.index(x)]