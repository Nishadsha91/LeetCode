class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()    
        rev = []       

        for w in words:           
            reversed_word = w[::-1]    
            rev.append(reversed_word) 

        return " ".join(rev)  
        