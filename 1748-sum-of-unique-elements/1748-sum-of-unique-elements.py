class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq ={}
        for n in nums:
            freq[n] = freq.get(n,0)+1
        
        total=0
        for n,count in freq.items():
            if count == 1:
                total += n
        return total

        