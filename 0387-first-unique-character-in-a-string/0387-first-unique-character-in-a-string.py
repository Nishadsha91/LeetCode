class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: count frequency manually
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        # Step 2: find first unique
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1

        