class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        

        if ch not in word:
            return word

        idx = word.index(ch)
        prefix_reversed = word[:idx+1][::-1]
        return prefix_reversed + word[idx+1:]
        