class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #create answer array
        n = len(arr)
        ans = [0] * n
        #initialize rightMax
        rightMax = -1
        # this is importand because the last element has no elements to its right so its preplacement should be -1
        for i in range(n -1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans