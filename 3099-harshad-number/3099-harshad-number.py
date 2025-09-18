class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        w = str(x)
        total = 0

        for i in w:
            total = total + int(i)
        if x % total == 0:
            return total
        return -1

 
        
