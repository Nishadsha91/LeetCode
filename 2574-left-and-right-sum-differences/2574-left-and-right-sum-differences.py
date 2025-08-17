class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)   
        left = 0
        ans = []

        for num in nums:
            right = total - left - num 
            ans.append(abs(left - right))
            left += num                  
        return ans
