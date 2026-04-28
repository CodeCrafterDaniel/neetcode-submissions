class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)

        if n == 0:
            return 0

        l, r = 0, n-1
        res = 0

        leftMax, rightMax = h[l], h[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, h[l])
                res += leftMax - h[l]
            else:
                r -= 1
                rightMax = max(rightMax, h[r])
                res += rightMax - h[r]
        
        return res
