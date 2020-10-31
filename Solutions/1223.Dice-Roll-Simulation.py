"""
1223. Dice Roll Simulation

A die simulator generates a random number from 1 to 6 for each roll. 
You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. 
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. 
In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, 
therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
 
Constraints:

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15
"""



"""
solution 1: backtrack - O(6^N) in worst case
"""
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def backtrack(curr_roll, curr_comb):
            if curr_roll == n:
                self.res += 1
                return
            
            for num in [1, 2, 3, 4, 5, 6]:
                if len(curr_comb) >= rollMax[num-1] and \
                all(cons_num == num for cons_num in curr_comb[-rollMax[num-1]:]):
                    continue      # 如果已经加了好几个相同的num了，那么这个num就不能再继续加入了
                curr_comb.append(num)
                backtrack(curr_roll + 1, curr_comb)
                curr_comb.pop()
                
        
        self.res = 0
        backtrack(0, [])
        return self.res
        
        
"""
solution 1: a little modified backtrack - O(6^N) in worst case.
不需要传入curr_comb, 只需要last_num和the repeat time of last_num
"""
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def backtrack(curr_roll, last_num, repeat_time):
            """
            不需要传入curr_comb, 只需要last_num和the repeat time of last_num
            """
            if curr_roll == n:
                self.res += 1
                return
            
            for num in [1, 2, 3, 4, 5, 6]:
                if num == last_num:
                    if repeat_time >= rollMax[num-1]:     # 如果已经加了好几个num了，
                        continue                        # 那么这个num就不能再继续加入了
                    backtrack(curr_roll + 1, num, repeat_time + 1)
                else:
                    backtrack(curr_roll + 1, num, 1)
                
        
        self.res = 0
        backtrack(0, -1, -1)    
        return self.res
        
        
"""
solution 2: backtrack + memo - O(6n^2).
套backtrack + memo的模板即可
"""
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def backtrack(curr_roll, last_num, repeat_time):
            if (curr_roll, last_num, repeat_time) in memo:
                return memo[(curr_roll, last_num, repeat_time)]
            
            if curr_roll == n:
                return 1
            if curr_roll > n:
                return 0
            
            res = 0
            for num in [1, 2, 3, 4, 5, 6]:
                if num == last_num:
                    if repeat_time >= rollMax[num-1]:   # 如果已经加了好几个num了，
                        continue                        # 那么这个num就不能再继续加入了
                    res = (res + backtrack(curr_roll + 1, num, repeat_time + 1) % MOD) % MOD 
                else:
                    res = (res + backtrack(curr_roll + 1, num, 1) % MOD) % MOD
            
            memo[(curr_roll, last_num, repeat_time)] = res
            return res
                
        
        MOD = 10**9 + 7
        memo = collections.defaultdict(int)   # (curr_roll, last_num, repeat_time) --> how many ways
        return backtrack(0, 0, 0)    
