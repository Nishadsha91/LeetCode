class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        wrd = s.split()
        res = " ".join(wrd[:k])
        return res
        
        