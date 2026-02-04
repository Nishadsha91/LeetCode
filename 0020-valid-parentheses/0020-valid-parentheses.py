class Solution(object):
    def isValid(self, s):
        stc = []
        mapping = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in '([{':
                stc.append(i)
            else:
                if not stc:
                    return False

                top = stc.pop()

                if mapping[i] != top:
                    return False

        return len(stc) == 0
