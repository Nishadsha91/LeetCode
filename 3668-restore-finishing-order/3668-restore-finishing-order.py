class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        out = []

        for i in order:
            if i in friends:
                out.append(i)
        return out