class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Step 1: place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        # Step 2: find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
