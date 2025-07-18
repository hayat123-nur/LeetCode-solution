class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lists=[]
        for word in words:
            morse=""
            for char in word:
                morse+=morse_code[ord(char)-97]
            if morse not in lists:
                lists.append(morse)
        return (len(lists))