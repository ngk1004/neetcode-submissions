class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check for the number of characters using the len in python
            return False
        return sorted(s) == sorted(t)