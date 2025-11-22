class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        vowels = 'aeiou'

        for i in s:
            freq[i] = freq.get(i, 0) +1
        
        max_vowel = 0
        max_consonant = 0

        for i, count in freq.items():
            if i in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)

        return max_vowel + max_consonant
