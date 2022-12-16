class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        low = 0
        high = max(piles)

        while low < high:

            mid = (low + high)//2

            eaten = 0

            for pile in piles:

                eaten += (pile+mid-1)//mid


            if eaten <= h:
                high = mid 
            else:
                low = mid + 1
        return low
                
"""
Suppose the pile has `pile` bananas and the eating speed is `mid` bananas per hour. The number of hours needed to eat all the bananas is pile/mid. However, this expression might not be an integer (for example, if pile=5 and mid=2, it would take 2.5 hours to eat all the bananas).

To handle this case, we can use integer division (//) to round the result down to the nearest integer. For example, 5//2 is equal to 2. The expression (pile+mid-1)//mid is equivalent to (pile/mid)+1, which rounds up instead of down. This ensures that the minimum number of hours needed to eat all the bananas in a pile is always at least 1.

Finally, we add up the minimum number of hours needed for each pile by using the eaten variable. This gives us the total number of hours needed to eat all the bananas.
"""

"""
 input piles = [3, 6, 7, 11] and h = 8:

    - The value of low is initialized to 0 and the value of high is initialized to the maximum value in piles, which is 11.
    - The loop begins with low equal to 0 and high equal to 11.
    - The value of mid is calculated as (low + high) // 2, which is equal to 5.
    - The loop iterates over the piles. For each pile, the expression (pile+mid-1)//mid is used to calculate the minimum number of hours needed to eat all the bananas in the pile. The value of eaten is incremented by this amount.
    - For the first pile (3 bananas), the expression evaluates to (3+5-1)//5 = 1, so the value of eaten is incremented by 1.
    - For the second pile (6 bananas), the expression evaluates to (6+5-1)//5 = 2, so the value of eaten is incremented by 2.
    - For the third pile (7 bananas), the expression evaluates to (7+5-1)//5 = 2, so the value of eaten is incremented by 2.
    - For the fourth pile (11 bananas), the expression evaluates to (11+5-1)//5 = 3, so the value of eaten is incremented by 3.
    - The value of eaten is now equal to 8, which is less than h. Therefore, the value of high is updated to mid, which is 5.
    - The loop iterates again with low equal to 0 and high equal to 5. The value of mid is now equal to 2.
    - The loop iterates over the piles again, and the value of eaten is recalculated. This time, eaten is equal to 9, which is greater than h. Therefore, the value of low is updated to mid + 1, which is 3.
    - The loop iterates again with low equal to 3 and high equal to 5. The value of mid is now equal to 4.
    - The loop iterates over the piles again, and the value of eaten is recalculated. This time, eaten is equal to 8, which is equal to h. Therefore, the loop terminates and the function returns 4.

So the minimum eating speed that allows you to eat all the bananas in h hours or less is 4 bananas per hour.
"""