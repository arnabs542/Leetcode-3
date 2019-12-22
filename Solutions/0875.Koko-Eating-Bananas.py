Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

 

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
 

Note:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9


"""If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left."""
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lens = len(piles)
        start, end = 0, max(piles)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isPossible(piles, H, mid):
                end = mid
            else:
                start = mid
        if self.isPossible(piles, H, end):
            return end
        if self.isPossible(piles, H, start):
            return start
            
    def isPossible(self, piles: List[int], H: int, K: int) -> bool:
        cntTime = 0
        for pile in piles:
            cntTime += (pile-1) // K + 1
        return cntTime <= H

"""Time complexity is O(N*log(W)), N is the length of piles, W is the max(piles)"""
