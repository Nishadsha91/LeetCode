class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort() 
        missing = 0  

        for i in nums:
            if i == missing:
                missing += 1
        return missing


        
        