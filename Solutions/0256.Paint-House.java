256. Paint House

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
             
             
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0 
        
        dp = [[0] * 3 for _ in range(len(costs))]    
        # dp[i][j] means the minimum cost to paint house i to be color j
        
        # initialize
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]
            
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        
        return min(dp[-1])

      
      
class Solution {
    public int minCost(int[][] costs) {
        if (costs.length == 0) return 0;
        
        // dp[i][j] = the min cost to paint house i to be color j
        int[][] dp = new int[costs.length][3];
        for (int i = 0; i < costs.length; i++) {
            if (i == 0) {
                dp[i] = costs[i];
            } else {
                dp[i][0] = costs[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
                dp[i][1] = costs[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
                dp[i][2] = costs[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
            }
        }
        return Math.min(Math.min(dp[costs.length - 1][0], dp[costs.length - 1][1]), dp[costs.length - 1][2]);
    }
}
