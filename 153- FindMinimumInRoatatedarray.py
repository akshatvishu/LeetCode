class Solution:
    def findMin(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] <= arr[right]:
                # right array is sorted thus, min_val will be in the left hence, we igoner the right part!
                right = mid

            else:
                left = mid +1
        # arr[right] == arr[left] -> exit loop
        return arr[left]




# # To find max:

# if arr[mid] > arr[right]:
"""
For example, consider the following array: [3, 4, 5, 1, 2]. If arr[mid] > arr[right],
 then mid will be 2 and right will be 4. Since arr[2] = 5 > arr[4] = 2, the right half of the array is sorted. 
 Therefore, the maximum element must be in the left half of the array, which is [3, 4, 5]
"""