class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check for the number of characters using the len in python
            return False # Not same? not anangram
        return sorted(s) == sorted(t) # anything else gets sorted into the array because it matches for that then i assume