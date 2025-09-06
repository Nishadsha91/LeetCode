from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = Counter(s)
        t1 = Counter(t)

        for ch in t1:
            if t1[ch] != s1.get(ch , 0):
                return ch
        