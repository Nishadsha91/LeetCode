class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort() 
        # smallest = 1  

        # for num in nums:
        #     if num == smallest:
        #         smallest += 1

        # return smallest

        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1