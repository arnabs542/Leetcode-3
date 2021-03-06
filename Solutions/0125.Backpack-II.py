"""
125. Backpack II

There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.

What's the maximum value can you put into the backpack?

A[i], V[i], n, m are all integers.
You can not split an item.
The sum size of the items you want to put into backpack can not exceed m.
Each item can only be picked up once

Example 1:

Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
Output: 9
Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9
"""


"""
https://www.kancloud.cn/kancloud/pack/70125
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。
定义状态：即f[i][m]表示前i件物品恰放入一个容量为m的背包可以获得的最大价值。
f[i][m]=max{f[i-1][m], f[i-1][m-A[i]]+V[i]}
不放第i件物品，则可以获得的最大价值是前i-1件物品恰放入一个容量为m的背包可以获得的最大价值 f[i-1][m].
放第i件物品，则可以获得的最大价值是 V[i] + 前i-1件物品放入一个容量为m-A[i]的背包可以获得的最大价值
"""

class Solution:
    def backPackII(self, M, A, V):
        dp = [[0 for _ in range(M + 1)] for _ in range(len(A) + 1)]     # 注意buffer layer
        for i in range(1, len(A) + 1):
            for m in range(1, M + 1):
                dp[i][m] = dp[i-1][m]
                if m >= A[i-1]:
                    dp[i][m] = max(dp[i][m], dp[i-1][m-A[i-1]] + V[i-1])
                    
        return dp[len(A)][M]

    
    
        
        
"""
optimize space using rolling array cuz dp[i] depends only on dp[i-1]"""
class Solution:
    def backPackII(self, m, A, V):
        if not A:
            return 0
            
        lens = len(A)
        dp = [[0] * (m + 1) for _ in range(2)]

        for i in range(lens):
            
            dp[i % 2][0] = 0
            
            for j in range(1, m + 1):
                if i == 0:      # initialize
                    dp[i][j] = V[0] if A[0] <= j else 0
                    continue
                
                if A[i] <= j:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - A[i]] + V[i])
                
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                
        return dp[(lens - 1) % 2][m]
