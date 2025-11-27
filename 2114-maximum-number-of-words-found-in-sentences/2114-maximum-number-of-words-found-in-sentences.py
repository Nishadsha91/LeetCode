class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count = 0
        # wrd = sentences.split()

        for wrds in sentences:
            w = wrds.split()
            c = len(w)

            if c > count:
                count = c
        return count
        