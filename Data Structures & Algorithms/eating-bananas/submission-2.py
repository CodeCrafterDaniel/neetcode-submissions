class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k, piles):
            res = 0
            for pile in piles:
                res = pile // k + (pile % k != 0) + res
            
            return res <= h
            
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            if check(mid, piles):
                r = mid
            else:
                l = mid + 1 
        
        return r
