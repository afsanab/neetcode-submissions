class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for letter in s:
            if letter in s_dict:
                s_dict[letter] = s_dict[letter] + 1
            else:
                s_dict[letter] = 1
        for letter in t:
            if letter in t_dict:
                t_dict[letter] = t_dict[letter] + 1
            else:
                t_dict[letter] = 1

        if s_dict == t_dict:
            return True
        else:
            return False
#1. make the dict w/ the right letters from 1st str + count
#2. repeat step 1 for 2nd str
# check if 2 dicts are the same pr not