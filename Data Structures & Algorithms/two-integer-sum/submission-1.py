class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ch = dict()
        for i, num in enumerate(nums):
            if target - num in ch:
                return [ch[target - num], i]
            ch[num] = i
