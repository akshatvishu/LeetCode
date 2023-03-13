
### Problem Statement
"""A group of two or more people wants to meet and 
minimize the total travel distance. You are given a 
2D grid of values 0 or 1, where each 1 marks the 
home of someone in the group. 
The distance is calculated using Manhattan Distance,
 where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
"""
## Example:
"""
Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]] 

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.
"""

#  grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]

import random


def quickselect(nums, k):
    if len(nums) == 1:
        return nums[0]
    
    pivot = random.choice(nums)

    lows = [el for el in nums if el < pivot]
    highs = [el for el in nums if el > pivot]
    pivots = [el for el in nums if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
     
def minTotalDistance(grid):
    col, rows = [], []

    for i, row in enumerate(grid): # rows of grid
        for j, val in enumerate(row): # col of the current row

            if val == 1:
                col.append(j) # col idx
                rows.append(i) # row idx

    # col.sort()
    # rows.sort()

    res = 0
    total_travel_distance = (quickselect(rows, len(rows) // 2),
                             quickselect(col, len(col) // 2))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += (abs(i - total_travel_distance[0]) + 
                         abs(j - total_travel_distance[1]))
    
    return res

grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]

print(minTotalDistance(grid=grid))