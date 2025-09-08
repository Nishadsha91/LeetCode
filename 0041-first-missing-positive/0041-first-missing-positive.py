class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        smallest = 1  

        for num in nums:
            if num == smallest:
                smallest += 1

        return smallest

