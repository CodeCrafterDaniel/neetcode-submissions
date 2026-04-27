class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ch = set()
        for num in nums:
            if num in ch:
                return True
            ch.add(num)
        return False