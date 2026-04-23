class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(sort(nums)) != len(sort(nums)):
            return True
        else:
            return False
        