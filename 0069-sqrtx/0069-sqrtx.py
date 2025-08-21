from math import sqrt

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        squared = sqrt(x)
        return int(squared)
        