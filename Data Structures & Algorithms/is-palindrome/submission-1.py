class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_check = ""
        for letter in s:
            if letter.isalpha() == True:
                pal_check += letter.lower()
        if pal_check == pal_check[::-1] and len(pal_check) > 1:
            return True
        else:
            return False