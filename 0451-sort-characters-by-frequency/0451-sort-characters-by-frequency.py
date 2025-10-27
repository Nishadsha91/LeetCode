class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1
        # srt = sorted(" ".join(freq))
        srt = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # return srt
        return "".join(ch * count for ch, count in srt)

        

       
        