class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in range(2):
            for num in range(nums):
                ans.append(num)
        return ans
