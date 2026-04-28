class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        l, r = 0, n-1

        res = 0
        
        while l < r:
            vol = min(h[l], h[r]) * (r - l)
            res = max(res, vol)

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        
        return res
