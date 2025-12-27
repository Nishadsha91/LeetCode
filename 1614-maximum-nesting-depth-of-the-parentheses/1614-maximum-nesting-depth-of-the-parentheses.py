class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        out = 0
        for i in s:
            if i == '(':
                depth += 1
                out = max(out , depth)
            elif i == ')':
                depth -= 1
        return out
        