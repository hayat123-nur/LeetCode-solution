class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        a={}
        for num in arr1:
            if num in a:
                a[num]+=1
            else:
                a[num]=1
        b=[]
        for num in arr2:
            if num in a:
                b.extend([num]*a[num])
                del a[num]
        for num in sorted(a):
            b.extend([num]*a[num])
        return b