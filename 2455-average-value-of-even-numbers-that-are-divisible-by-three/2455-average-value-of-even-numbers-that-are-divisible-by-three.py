class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = 0
        out = 0

        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                out += i
                lis += 1

        return out // lis if lis > 0 else 0
        
