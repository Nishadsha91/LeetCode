class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        without_dup = set()
        
        for i in nums:
            if i in without_dup:
                return i
            without_dup.add(i)
        