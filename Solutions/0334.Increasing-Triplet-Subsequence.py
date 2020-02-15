"""solution 1: same as 300
O(N^2), O(N)"""
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        lens = len(nums)
        if lens < 3:
            return False
        
        dp = [1] * lens

        for j in range(1, lens):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
            if dp[j] >= 3:
                return True
            
        return False
"""    
"""how to solve it in O(N), O(1)"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        lens = len(nums)
        if lens < 3:
            return False
        
        # min_1, mnin_2 and are the most min and the second min in the array
        min_1, min_2 = float("inf"), float("inf")
        for num in nums:
            if num < min_1:             # first renew
                min_1 = num              
            elif min_1 < num < min_2:   # second renew
                min_2 = num
            elif min_2 < num:           # third renew
                return True
            
        return False
