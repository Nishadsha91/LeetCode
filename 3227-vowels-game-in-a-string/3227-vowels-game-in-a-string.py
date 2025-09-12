class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = 'aeiou'
        for w in s:
            if w in vowels:   
                return True
        return False 

        