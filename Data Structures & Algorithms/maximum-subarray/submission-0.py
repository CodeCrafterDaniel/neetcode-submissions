class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        c_sum = 0
        ans = nums[0]
        for r in range(n):
            c_sum += nums[r]
            ans = max(c_sum, ans)
            if c_sum < 0:
                l = r
                c_sum = 0
        
        return ans