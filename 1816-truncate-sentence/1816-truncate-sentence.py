class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        wrd = s.split()
        return " ".join(wrd[:k])
        
        