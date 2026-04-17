class Solution:
    def isPalindrome(self, s: str) -> bool:
        #'' is the empty start string, c.lower() makes it lower case
        #for c in s, looping thru each value in s
        #if c.isalnum(), checking if valid value
        #.join adds the c values that passed into ''
        stripped = ''.join(c.lower() for c in s if c.isalnum())
        return stripped == stripped[::-1]