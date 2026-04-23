class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       ans = []
       for i in range(nums):
            for num in nums:
                ans.append(num)
            return ans