class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        spos = 0

        for char in t:
            if char == s[spos]:
                spos += 1
            if spos == len(s):
                return True
        
        return False

               
        