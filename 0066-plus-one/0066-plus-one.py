class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        word = ''.join(map(str,digits))
        num = int(word) + 1
        return [int(d) for d in str(num)]
        