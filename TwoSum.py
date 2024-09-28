class Solution(object):
    def twoSum(self, nums, target):
        indexes = {}
        for i in range(len(nums)):
            add = target - nums[i]
            if add in indexes:
                return [indexes[add], i]
            indexes[nums[i]] = i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
