import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        res = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        first_max = heapq.heappop(heap)
        res.append(-first_max[0])
        heapq.heappush(heap, first_max)

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            max_el = heapq.heappop(heap)
            while max_el[1] <= i-k:
                max_el = heapq.heappop(heap)

            res.append(-max_el[0])
            heapq.heappush(heap, max_el)
        
        return res
