class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        paired = zip(heights, names)
        pair = sorted(paired, reverse=True)
        return [name for height, name in pair]
