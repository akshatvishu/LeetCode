'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Constraints:

- 1 <= nums.length <= 105
- 104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

time complexity must be better than O(n log n), where n is the array's size.
''' 

# Approach - Max_Heap


from typing import List
import heapq
from collections import Counter

# nums = [1,1,2,2,3,1,2,3,3,3,1,1,1,4]
# def topKFrequentElements( nums: List[int], k: int) -> List[int]:

#     freq = Counter(nums)
#     print(f'freq= {freq}')
#     heap = [(v,k)for k,v in freq.items()]
#     heapq.heapify(heap)
#     print(f'heap={heap}')

#     if len(heap) > k: 
#         heapq.heappop(heap)
#     return [k for v,k in heap]

# print(topKFrequentElements(nums=nums, k=3))
from collections import defaultdict

from collections import Counter


# def topK(nums, k):

#     buckets = [[] for _ in range(len(nums)+1)]

#     freq = Counter(nums).items()

#     for k, v in freq:
#         buckets[v].append(k)
    
#     result = [] 

#     for i in range(len(buckets)-1, -1, -1):
#         result.extend(buckets[i])



def topKFrequent(nums, k):
    bucket = [[] for _ in range(len(nums) + 1)]
    Count = Counter(nums).items()
    print(f'Count = {Count}')
    for num, freq in Count:
        bucket[freq].append(num)
    print(f'bucket = {bucket}')
    flat_list = []
    for i in range(len(bucket)-1, -1, -1):
        flat_list.extend(bucket[i])
    print(f'flat_list = {flat_list}')
    return flat_list[:k]


    
print(topKFrequent(nums = [4,4,4,5,5,6,6,6,6],k = 2))
    
    
    

    


# Bucket Sort - O(n)
# def topKFrequentElements( nums: List[int], k: int) -> List[int]:

#     # Create a dict of nums 
#     freq = Counter(nums)

#     # Create a buckets of size nums + 1
#     buckets = [[] for _ in range(len(nums) + 1) ]
#     #print(f'Buckets after creation = {buckets}')

#     for k, v in freq.items():
#         buckets[v].append(k)
#     #print(f'buckets = {buckets}')

#     #
#     result = []

#     for i in range(len(buckets)-1, -1, -1):
#         result.extend(buckets[i])

#         if len(result) >= k:
#             break

#     return result[:k]
        
        





