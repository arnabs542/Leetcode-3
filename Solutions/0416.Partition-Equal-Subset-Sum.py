"""
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
 
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""



"""
背包问题：将A中的物品放入容量为target的背包中，问是否存在？
f[i]=将前i个物品放入背包中，能否拼出t (背包问题重量一定要入状态)
f[i][t]=True if 不放最后一个进背包: f[i-1][t]=True or 放最后一个进背包: f[i-1][t-A[i-1]]=True"""
"""
dp[i][m]=can fill up to m using the nums till ith, not including i
dp[i][m] = 1. not put nums[i-1]: dp[i-1][m] or put nums[i-1]: dp[i-1][m-nums[i-1]]
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target != int(target): return False
        target = int(target)
        
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for m in range(1, target + 1):
                dp[i][m] = dp[i-1][m]
                if m >= nums[i-1]:
                    dp[i][m] = dp[i][m] or dp[i-1][m-nums[i-1]]
        return dp[-1][-1]
       
       
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # select some nums to sum up to sum/2, if sum/2 is not int, then not possible
        # dp[i][s] = can selecet from 0th to ith number to ad to s?
        # dp[i][s] = true if dp[i-1][s] is true
        # if dp[i-1][s] is false: dfp[i][s]=dp[i][s-num]
        # dp[0][s]=false, dp[i][0]=false, dp[0][0] = true
        # return dp[lens][sum/2]
        
#         # 1  2  5
#           0 1 2 3 4     s
# #      0  T F F F F 
# #      1  T T F F F
# #      2  T T T T F
# #      3  T T T T F
# #      i
        
        lens = len(nums)
        if lens <= 1:
            return False
        
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2
        
        dp = [[False] * (target + 1) for _ in range(lens + 1)]
        dp[0][0] = True
        
        for i in range(1, lens + 1):
            for s in range(target + 1):
                if s == 0:
                    dp[i][s] = True
                    continue
                    
                if dp[i - 1][s]:
                    dp[i][s] = True
                else:
                    if s >= nums[i - 1] and dp[i - 1][s - nums[i - 1]]:
                        dp[i][s] = True
                        
        return dp[lens][target]
