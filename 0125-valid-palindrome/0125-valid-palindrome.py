import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = re.sub(r'[^a-z0-9]', '' , s.lower())
        if word == word[::-1]:
            return True
        else:
            return False
        