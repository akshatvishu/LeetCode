### Rotated Array:
"""
A rotated array is an array that has been rearranged by rotating its elements by a certain number of positions
in a circular fashion. For example, the array [1, 2, 3, 4, 5] rotated by two positions would become [3, 4, 5, 1, 2].

"""

# Function to rotate an array in python:

# Slice the array from the position to the end and add it to the slice from the beginning to the position.
# def rotate_arr(arr, pos):

#     return arr[pos:] + arr[:pos]


# # Another way to implement it will be to use the rotate() function from the collections module.

# from collections import deque,rotate 

# def rotate_arr(arr, pos):
#     d = deque(arr)
#     d.rotate(pos)
#     return list(d)


# # Another way to rotate it will be : 

# def rotate_arr(arr,pos):

#     rotated_arr = []

#     for i in range(len(arr)):
#         rotated_arr.append(arr[(i+pos)%len(arr)]) # What it does  is that it takes the index of the element and adds the position to it and then takes the modulus of the length of the array.  This way, it will always be within the range of the array.
#     return rotated_arr


###################################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while left <= right:

            mid = (left + right) //2

            if nums[mid] == target:
                return  mid 
            # if the left side is sorted
            if nums[left] <= nums[mid]:
                # left side is sorted
                if nums[left] <= target < nums[mid]:
                    # target is in the left side of the array
                    right = mid - 1  
                else:
                    # target is in the right side of the array
                    left = mid + 1
            else:
                # right side is sorted
                if nums[mid] < target <= nums[right]:
                    # target is in the right side of the array
                    left = mid + 1
                else:
                    # target is in the left side of the array
                    right = mid - 1
        return -1

## Explanation :
"""
To use binary search on a rotated sorted array, you need to first determine which half of the array is sorted.
 This can be done by comparing the first element with the last element. If the first element is less than the last element, 
 then the entire array is sorted and you can perform a regular binary search.

 Binary search is an efficient algorithm that can be used to search for an element in a sorted array. It works by repeatedly dividing the array in half until the element is found or it is clear that the element is not present in the array.

To use binary search on a rotated sorted array, you need to first determine which half of the array is sorted. This can be done by comparing the first element with the last element. If the first element is less than the last element, then the entire array is sorted and you can perform a regular binary search.

If the first element is greater than the last element, then the array is rotated and one half of the array is sorted. 
To determine which half is sorted, you can compare the target element with the middle element of the array.
If the target element is greater than the middle element, then the sorted half of the array is on the right. 
If the target element is less than the middle element, then the sorted half of the array is on the left.
"""