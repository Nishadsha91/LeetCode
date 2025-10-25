class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for i in nums:
            if i % 2 == 0:
                out.append(0)
            else:
                out.append(1)
        return sorted(out)
        