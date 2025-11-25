class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        wrd = s.split()
        sentence = []

        for i in wrd:
            pos = int(i[-1])
            word = i[:-1]
            sentence.append((pos,word))

        sentence.sort(key=lambda x: x[0])

        ordered =[]

        for p,w in sentence:
            ordered.append(w)

        return " ".join(ordered)


        



        