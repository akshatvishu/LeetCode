# Min + Max Heap to find Median
import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    

    def addNum(self, num:int) -> None:
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
    

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    

    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return(self.min_heap[0] -  self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]


# Rivest-Tarjan-Selection algorithm 
# Or median-of-medians algorithm - O(n)
        

# class MedianFinder:

#     def __init__(self):
#         self.nums = []
        

#     def addNum(self, num: int) -> None:
#         self.nums.append(num)
        

#     def findMedian(self) -> float:
#         k = len(self.nums) // 2
#         if len(self.nums) % 2 == 1:
#             return self.medianOfMedians(self.nums, k)
#         else:
#             return (self.medianOfMedians(self.nums, k) + 
#                     self.medianOfMedians(self.nums, k-1)) / 2


#     def medianOfMedians(self, nums, k):
#         if len(nums) <= 5:
#             return sorted(nums)[k]
#         sublists = [nums[j:j+5] for j in range(0, len(nums), 5)]
#         medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
#         pivot = self.medianOfMedians(medians, len(medians) // 2)
#         lows = [el for el in nums if el < pivot]
#         highs = [el for el in nums if el > pivot]
#         if k < len(lows):
#             return self.medianOfMedians(lows, k)
#         elif k < len(nums) - len(highs):
#             return pivot
#         else:
#             return self.medianOfMedians(highs, k - (len(nums) - len(highs)))
        


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()