class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cnt = 0

        for i in nums:
            if cnt == 0:
                ans = i
                cnt = 1
            elif i == ans:
                cnt += 1
            else:
                cnt -= 1

        return ans
