class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        out = []
        for i in address:
            if '.' in i:
                out.append('[.]')
            else:
                out.append(i)
        return "".join(out)

        