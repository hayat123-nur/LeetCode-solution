class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        nl=[]
        list=[]
        for i in range(len(names)):
            list.append((heights[i],names[i]))
            list.sort(reverse=True)
        for i in list:
            nl.append(i[1])
        return nl