class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=''.join(char for char in s if char.isalnum())
        cleaner=clean.lower()
        if cleaner== cleaner[::-1]:
            return True
        else:
            return False
        

        