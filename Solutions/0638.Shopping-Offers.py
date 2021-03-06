"""
638. Shopping Offers

In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, 
and the number we need to buy for each item. The job is to output the lowest price you have to pay for exactly certain items as given, 
where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, 
other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
"""


"""
backtrack结束条件: the needs has been met: all(curr_bought[i] > needs[i] for i in range(len(needs)))
constraint on next_candidates: 题目要求You are not allowed to buy more items than you want, even if that would lower the overall price.
arguments pass into backtrack function: curr_bought, curr_cost
O(2^M*L*N) where L is len(prices), M is how many specials are there, N is value of needs
"""
class Solution:
    def shoppingOffers(self, prices: List[int], specials: List[List[int]], needs: List[int]) -> int:
        def backtrack(curr_bought, curr_cost):
            if all(curr_bought[i] >= needs[i] for i in range(n)):
                self.min_cost = min(self.min_cost, curr_cost)
                
            for special in specials:
                if any(special[i] > needs[i] - curr_bought[i] for i in range(n)):    
                    continue    # You are not allowed to buy more items than you want, even if that would lower the overall price.
                next_bought = [curr_bought[i] + special[i] for i in range(n)]
                backtrack(next_bought, curr_cost + special[-1])
                                
                
        n = len(needs)
        for i, price in enumerate(prices):      # 第一步：把单买的方式也转换成specials
            alone = [0 for _ in range(n)]
            alone[i] = 1
            alone.append(price)
            specials.append(alone)
        
        self.min_cost = sys.maxsize
        backtrack([0 for _ in range(n)], 0)
        return self.min_cost
        
        
        
"""
solution 2: dfs + memorization 
- O(MLN) where L is len(prices), M is how many specials are there, N is value of needs
"""
class Solution:
    def shoppingOffers(self, prices: List[int], specials: List[List[int]], needs: List[int]) -> int:
        def backtrack(curr_bought):
            if all(curr_bought[i] == needs[i] for i in range(n)):
                return 0
                
            if tuple(curr_bought) in memo:
                return memo[tuple(curr_bought)]
                
            res = sys.maxsize
            for special in specials:
                if any(special[i] > needs[i] - curr_bought[i] for i in range(n)):   # You are not allowed to buy more items than you want, 
                    continue                        # even if that would lower the overall price.
                next_bought = [curr_bought[i] + special[i] for i in range(n)]
                res = min(res, special[-1] + backtrack(next_bought))
                               
            memo[tuple(curr_bought)] = res
            return res
                
        n = len(needs)
        for i, price in enumerate(prices):      # 第一步：把单买的方式也转换成specials
            alone = [0 for _ in range(n)]
            alone[i] = 1
            alone.append(price)
            specials.append(alone)
        
        memo = defaultdict(int)     # curr_bought --> from curr_bought, what is the minimum cost to meet needs
        return backtrack([0 for _ in range(n)])     # returns from curr_bought, what is the minimum cost to meet needs
