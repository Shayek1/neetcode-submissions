class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sList = []
        tList = []

        for char in s:
            sList.append(char)
        
        for char in t:
            tList.append(char)
        
        if sorted(sList) == sorted(tList):
            return True
        else:
            return False