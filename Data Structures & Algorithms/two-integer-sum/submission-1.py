class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} #val indicies
        for i in enumerate(nums):
             diff = target - n
             if diff in prev_map:
                return [prev_map[diff], i]
             prev_map = i
        return