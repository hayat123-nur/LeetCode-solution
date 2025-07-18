class Solution():
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        same_row=[]
        for word in words:
            lower_word=word.lower()
            if all(char in row1 for char in lower_word):
                same_row.append(word)
            elif all(char in row2 for char in lower_word):
                same_row.append(word)
            elif all(char in row3 for char in lower_word):
                same_row.append(word)

        return same_row

