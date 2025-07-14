class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        sort_words=sorted(a,key=lambda x:x[-1])
        sort_words=[b[:-1] for b in sort_words]
        word=" ".join(sort_words)
        return word



        