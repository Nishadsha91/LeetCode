class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        w = str(x)
        if w == w[::-1]:
            return True
        else:
            return False
        