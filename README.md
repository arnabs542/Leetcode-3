## 三刷：不做新题了，就这300题！目标是刷熟练！模板总结出来天天拿出来背诵！
## 每日Review：06/01 - 06/15
06/01-0334; 06/02-0010; 06/03-0173; 06/04-0480; 06/05-0212; 06/10-0752





# [Data Stream and Multiple Query]()
- [0243. Shortest Word Distance](Solutions/0243.Shortest-Word-Distance.py) (E) <br>
Should know both two pass solution and One pass solution. follow up 1:  如果word1在words中很少只有两个，word2在words中很多有1 million个，怎么优化算法？那么这时候solution 1就派上用场了，我们可以存下idx1 和 idx2两个list. eg: idx1 = [10, 50000]; idx2 = [.......], 那么我们可以在idx2中binary search离10最近的数，然后binary search离50000最近的数。这样时间复杂度就是O(MlogN)了。
Follow up 2:
如果题目改成不是求两个word的最短距离而是是求K个word的最短距离呢？ solution 1: leetcode 76. Minimum Window Substring.  O(N) where N is the the lens of words.  soltution 2: leetcode 23. Merge k Sorted Lists.  O(NlogK), 方法与solution 1类似，只是为了知道k个idx list中哪根指针需要往前移动一下, 我们需要一个heapq, heapq中最小的那个往前挪动一步.
- [0244. Shortest Word Distance II](Solutions/0244.Shortest-Word-Distance-II.py) (!!M) <br>
如果题目要求multiple query with unlimited time, 那么一定考察的是precomputation!! precomputation记录结果一般都需要一个hash map!! 
这个思想非常重要！！这个题用dictionary记录每个word在words中的位置，这样如果这次需要query a and b, 下次需要query c and d, 
我们都可以很快找到他们的位置。    # 注意可能会有重复的query，比如第一次query a and b, 第三次又需要query a and b, 这时候为了为了避免重复计算，我们可以直接用memo/cache保存query a and b 的结果, 这个思想非常重要！！这个思想成立的前提是memory不值钱！Follow up 1: 
你都用两个额外空间去存结果以达到加速的目的了（一个是dictinoary存放每个word在words中的位置，另一个是cache/memo记录已经query过的a and b的结果）,可是面试官还不开心，他还希望调用 query method 能更快一些，怎么办？那咱们就采用最极端的方法：把所有words里可能的word1 and word2组合的结果都算出来存到cache中，这样所有的query 就都是O(1)了这个方法的前提是words list是不会变的，如果重新instantiate一个class把constrcutor里的words list变了那之前的所有结果就都白算了。
- [245. Shortest Word Distance III](Solutions/0245.Shortest-Word-Distance-III.py) (M) <br>
word1 and word2 may be the same and they represent two individual words in the list. 分word1等于和不等于两种情况讨论就可以了。



# [Dynamic Programming/bottom up](Dynamic-Programming.py)
### [Recursion with memoization/top down](/Dynamic-Programming.py)
139. word break; 312. Burst Balloons
使用记忆数组 memo 的递归写法，和使用 dp 数组的迭代写法，乃解题的两大神器，凡事能用 dp 解的题，一般也有用记忆数组的递归解法，好似一对形影不离的好基友～何时用带memo的recursion? 如果用dp的转移方程很复杂，那就用带memo的recursion, 一定要会默写！


### [坐标型DP](/Dynamic-Programming.py)
- [0062. Unique Paths](Solutions/0062.Unique-Paths.py) (!!M) <br>
状态: f[i][j]=有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = f[i][j-1]+f[i-1][j]
- [0063. Unique Paths II](Solutions/0063.Unique-Paths-II.py) (M) <br> 
转移方程：f[i][j] = 0 if it is obstacle else f[i][j-1]+f[i-1][j])
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M) <br> 
dp[i][j]=the minimum path sum to (i, j); dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
- [0120. Triangle](Solutions/0120.Triangle.py) (M) <br>
dp[i][j] = min(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1]), rolling array to reduce space to O(N)
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M) <br>
dp[i][j]=以(i, j)为右下角的最大正方形的边长; dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j]=1 
- [0403. Frog Jump](Solutions/0403.Frog-Jump.py) (M) <br>
维护一个stonesDict的key is the stone in stones. value is the possible steps to reach the stone.
There could be multiple possible steps to reach the stone, so stonesDict[stone] = set(). 
状态转移方程为：1. 跳k-1到stone+k-1: stonesDict[stone + k - 1].add(k - 1); 2. 跳k到stone + k: stonesDict[stone + k].add(k); 3. 跳k + 1到stone + k + 1:stonesDict[stone + k + 1].add(k + 1); Return stonesDict[last stone] is not empty; this is bottom up method O(N^2), O(N^2)
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!H) <br>
存在性问题。状态: dp[j]=能不能跳到位置j; 转移方程：dp[j]=True if dp[i] and nums[i]>=j-i) (TLE 注意只要有一个dp[i]是的dp[j]=True了就可以break了). DP解法: O(N^2).  Greedy 解法: O(N) Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index (currPosition + nums[currPosition] >= GoodIndex). If we can reach a GOOD index, then our position is itself GOOD. Iteration continues until the beginning of the array.  Return if the first position is a GOOD index.

### [序列型DP](/Dynamic-Programming.py)
- [0256. Paint House](Solutions/0256.Paint-House.py) (E) <br>
dp[i][j] means the minimum cost to paint house i to be color j; dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
- [0265. Paint House II](Solutions/0265.Paint-House-II.py) (H) <br> 
dp[i][j]=minimum cost to paint the ith house the be color j; dp[i][j] = dp(minIThe(i-1)thRow) + costs[i][j]. In order to find dp(minIThe(i-1)thRow fast), we can find the position for the 1st and 2nd min in the i-1 th row first, then in the ith row calcuation, if j=1stMinposition, then dp[i][j]=2nd_min + costs[i][j], else dp[i][j]=1st_min + costs[i][j]
- [0198. House Robber](Solutions/0198.House-Robber.py) (E) <br>
f[i]=the max profit when reaching ith house; f[i] = max(rob ith = f[i-2]+nums[i], not rob ith = f[i-1]) <br>
空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]
- [0213. House Robber II](Solutions/0213.House-Robber-II.py) (M) <br>
房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：1. 房子1没偷：问题变成了对房子2:N做House robber I的问题; 2. 房子N没偷：问题变成了对房子1:N-1做House robber I的问题
- [0337. House Robber III](Solutions/0337.House-Robber-III.py) (M) <br>
树状的house.递归： def with_without_rob(self, root): return a tuple, the 1st element in the tuple is the max profift with_rob_root， the 2nd element in the tuple is the max profit without_rob_root. 递归公式：with_rob_root = root.val + without_rob_left + without_rob_right; without_rob_root = max(with_rob_left, without_rob_left) + max(with_rob_right, without_rob_right)

### [Buy and sell stock DP问题](/Dynamic-Programming.py)
- [0121. Best Time to Buy and Sell Stock](Solutions/0121.Best-Time-to-Buy-and-Sell-Stock.py) (E) <br>
Only one transaction is allowed.  Maintain a minPrice and a maxProfit; maxProfit = max(maxProfit, price - minPrice)
- [0122. Best Time to Buy and Sell Stock II](Solutions/0122.Best-Time-to-Buy-and-Sell-Stock-II.py) (E) <br>
As many transaction as possible.  make a transaction every time price[i]>price[i-1]
- [0123. Best Time to Buy and Sell Stock III](Solutions/0123.Best-Time-to-Buy-and-Sell-Stock-III.py) (H) <br>
Only two transactions are allowed.  Maintain buy1=the minimum money you can **owe** after the first buy, sell1=the maximum money you **earn** after the first sell, also, buy2, sell2, and update them together in a for loop, 算法只是把121中的算法重复两次而已.
- [0188. Best Time to Buy and Sell Stock IV](Solutions/0188.Best-Time-to-Buy-and-Sell-Stock-IV.py) (H) <br>
Only k transactions are allowed.   Maintain buy=[]*k, sell=[]*k, and update them together in a for loop. buy[i] = min(buy[i], price - sell[i - 1]), buy[i] = the minimum money you can own after the ith purchase; sell[i] = max(sell[i], price - buy[i]), sell[i] = the maximum money you can earn after the ith purchase.  Solve the memory overflow problem: if k>prices.length/2, then it is the same as 122.
- [0309. Best Time to Buy and Sell Stock with Cooldown](Solutions/0309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py) (M) <br>
Has to rest for one day before buy another stock.  **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益, return unhold[-1] <br> 
hold[i] = max(hold[i-1], unhold[**i-2**]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i]) 学会画state machine
- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M) <br>
There is transaction fee when you sell. **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[i-1]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i] **- fee**)

###  [最长子序列问题](/Dynamic-Programming.py) (dp[i]都是定义为以i结尾的最长....)
- [0674. Longest Continuous Increasing Subsequence](Solutions/0674.Longest-Continuous-Increasing-Subsequence.py) (E) <br>
dp[i] = 以i结尾(包括i)的最长连续子序列; dp[i] = dp[i-1] + 1 if nums[i]>nums[i-1]; solution 2: 同向双指针（滑动窗口）
- [0300. Longest Increasing Subsequence](Solutions/0300.Longest-Increasing-Subsequence.py) (!!M) <br> --- 1048 --- 
不需要连续，所以不是dp[i] = dp[i-1] + 1，而是所有的j之前的i都有可能, 所以转移方程是 dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]) <br>
dp + binary search (O(NlogN))的算法也很重要！dp[i] = the maintianed array with i as the possible increadsing numbers, dp should be an orderd array: if nums[i] > the last item in dp, then append nums[i] to dp, if < the first item in dp, then replacethe first item with nums[i], if is in between, then将sorted arr中最接近num的数用num取代, by using binary search. same as 35. Search Insert Position
- [0354. Russian Doll Envelopes](Solutions/0354.Russian-Doll-Envelopes.py) (H) <br>
Similiar with 300. LIS; sort the list first envelopes.sort(key = lambda x: (x[0], x[1])), here we not only compare nums[j]>nums[i], but instead both the width and height; TLE. Solution 2: sort the evelopes first, then do LIS for the 2nd dimension of the evelopes O(nlogn) using the exact same way as 300.
- [0673. Number of Longest Increasing Subsequence](Solutions/0673.Number-of-Longest-Increasing-Subsequence.py) (M) <br>
 dp=以i为结尾的最大的长度; cnt=以i为结尾的最大的长度的个数; 在nums[j]>nums[i]的情况下：cnt[j]+=cnt[i] if dp[j]=dp[i]+1
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.Longest-Arithmetic-Sequence.py) (M) <br>
dp[i] = {key:diff, val:lens of arithmetic sequence ended with i and diff as 公差}; dp[j][nums[j]-nums[i]] = dp[i][nums[j] - nums[i]] + 1
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.Length-of-Longest-Fibonacci-Subsequence.py) (M) <br>
dp[i]=dictionary{key: last num of the fib; val: the lens of the fib ended with ith}, dp[j][nums[i]]=d[i][nums[j]-nums[i]]+1
- [0334. Increasing Triplet Subsequence](Solutions/0334.Increasing-Triplet-Subsequence.py) (M) <br>
Similiar with 300. LIS; dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]); if dp[j]>=3 return True；  how to solve it in O(N), O(1); min_1, min_2 and are the most min and the second min in the arr, if min_1 and min_2 are renewed twice already and there is a num>min_2 later, then return True.

### [区间型DP](/Dynamic-Programming.py) 自然而然将状态定义为f[i][j]表示面对子区间[i, j]时的最佳性质
- [0005. Longest Palindromic Substring](Solutions/0005.Longest-Palindromic-Substring.py) (!!M) <br>
题目问substring, substring就需要是连续的，题目要求Return the longest substr: dp[i][j]=from i to j (including j), is it a palindr? if s[i]==s[j]: dp[i][j] = dp[i+1][j-1]; 注意初始化对角线和相邻的，因为计算dp[i][j]需要用到dp[i+1][j-1]，所以要先算i+1, 再算i，所以i 是倒序遍历
solution Solution 2: central spread.  从中间c往两边遍历i--, j++，遍历两次：一次是i=c, j=c开始遍历， 一次是i=c, j=c+1开始遍历。
- [0516. Longest Palindromic Subsequence](Solutions/0516.Longest-Palindromic-Subsequence.py) (!!M) <br>
题目问subsequence, subsequence不需要连续，题目要求Return the longest length: dp[i][j]=longest palindr from i to j; dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1]);注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0312. Burst Balloons](Solutions/0312.Burst-Balloons.py) (!!H) <br>
带memo的recursion比DP更好懂; left = self.memoSearch(nums, i, k, memo); right=self.memoSearch(nums, k, j, memo); maxCoins = max(maxCoins, left + right + nums[i] * nums[k] * nums[j]). 
也可以用dp: https://qoogle.top/leetcode-312-burst-balloons/ <br>
Lintcode 476. Stone Game <br>
1011
410. Split Array Largest Sum
1444
###  [划分型DP](/Dynamic-Programming.py) (状态往往定义为前j个的某种特性，不包括j！！！！，这个思想很重要，相当于给前面做了一层buffer layer)
- [0139. Word Break](Solutions/0139.Word-Break.py) (!!M) <br>
dp[i]=can partition until ith char?, not including i; dp[j]=true if (for i < j, there is dp[i]=True and s[i:j]is in wordDict)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M) <br>
f[i]=number of decode ways until i (not including i); f[i]=f[i-1]+f[i-2] if int(s[i-2:i])<=26 else f[i-1]
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (M) <br>
f[j]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5); solution 2 mathematics: Four-square theorem states that every natural number can be represented as the sum of at most four integer squares.
- [0132. Palindrome Partitioning II](Solutions/0132.Palindrome-Partitioning-II.py) (!!H) <br>
子数组或者子字符串且求极值的题，基本就是 DP 没差了. f[j]=the minimum number of total palindrome till the jth character (not including j); f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome. O(N^3), 划分型的dp的状态一般都not include j, 这样就有一个buffer layer可以用。Solution 2: 优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，这样就不用每次都用双指针去判断s[i:j]是不是palindrome. 输出所有的可能的partition成palindrome的组合问题只能dfs+backtracking了- 131. Palindrome Partitioning


### [博弈型DP](/Dynamic-Programming.py)
- [0394. Coins in a Line](Solutions/0394.Coins-in-a-Line.py) (M Lintcode) <br>
Solution1 dp: f[i]=面对i个石子，先手是必胜吗; f[i]=True if f[i-1] or f[i-2] 有一个是False <br>
Solution 2: 至于prev, curr有关，所以可以空间优化成O(1)了; Solution 3 数学: 只要是3的倍数就一定输 return n % 3 != 0
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M) <br>
f[i][j]=当石子还剩i到j时，先手最多能赢多少; f[i][j] = max(取左边A[i]-f[i+1][j], 取右边A[j]-f[i][j-1]), 注意f[i][j]与f[i+1][j]相关，所以i要从后往前遍历.

### [背包型DP](/Dynamic-Programming.py)
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (!!M) <br>
背包问题，重量一定要入状态。状态: f[X]=最少用多少枚硬币拼出X; 转移方程：f[X] = min(f[X-1]+1, f[X-2]+1, f[X-5]+1, f[X])
- [0092. Backpack](Solutions/0092.Backpack.py) (!!M Lintcode) <br>
f[i][m]=能否用前i个物品拼出重量m; f[i][m] = f[i-1][m] (放不入，表示前i-1个物品就可以拼出m) or f[i-1][m-A[i-1]] (放入，表示前i-1个物品可以拼出m-A[i-1]); # 注意点1：这里要定义lens+1，这样就可以做一个buffer layer出来了; # 注意点2；这里循环i在外面，m在里面，千万别搞反了！！# 注意点3：由于buffer layer的存在，这里用nums[i-1]与m相比较
- [0563. Backpack-V](Solutions/0563.Backpack-V.py) (!!M Lintcode) <br>
一个num不能取多次，所以与322. coin change 不同。所以必须用二维数组，f[i][m]=前i个物品能拼出重量m有多少种方式。f[i][m] = 不放入 f[i-1][m] + 放入 f[i-1][m-A[i-1]] if m > nums[i] else =f[i-1][m]
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (!!M) <br> 
一个num能取多次，所以与322. coin change 相同。所以可以用一维数组，f[i]=how many ways to combine to number i; 背包问题一定要把总承重放到状态里！！ f[i]=f[i-A1]+f[i-A2]+f[i-A3].... <br>
- [0125. Backpack II](Solutions/0125.Backpack-II.py) (!!M Lintcode) <br>
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。用子问题定义状态：即f[i][j]表示前i件物品拼出重量j可以获得的最大价值。
f[i][j]=max{f[i-1][j] (不放入),f[i-1][j-A[i]]+V[i] (放入)}; return f[lens-1][M]
- [0089. k Sum](Solutions/0089.k-Sum.py) (M Lintcode) <br>
f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们的和是s; 情况一:（A[i-1]不选入）：需要在前n-1个数中选K个数，使得它们的和是Target: f[i][j][s] += f[i-1][j][s]; 情况二（A[i-1]选入）：需要在前i-1个数中选j-1个数，使得它们的和是Target-A[i-1]: f[i][j][s] += f[i-1][j-1][s-A[i-1]]
- [0416. Partition Equal Subset Sum](Solutions/0416.Partition-Equal-Subset-Sum.py) (M) <br>
背包问题：将A中的物品放入容量为target的背包中，问是否存在？一个num不能取多次，所以与322. coin change 不同。所以必须用二维数组。与0092一模一样。 f[i][t]=将前i个物品放入背包中，能否拼出t (背包问题重量一定要入状态); f[i][t]=True if 不放最后一个进背包: f[i-1][t]=True or 放最后一个进背包: f[i-1][t-A[i-1]]=True

### [位操作型DP](/Dynamic-Programming.py)
- [0338. Counting Bits](Solutions/0338.Counting-Bits.py) (M) <br>
状态dp[i]=i的二进制中有多少个1; dp[i] = dp[i >> 1] + i % 2

### [双序列型DP!!](/Dynamic-Programming.py) 
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (!!M) <br>
f[i][j]为A前i个字符A[0..i)和B前j个字符[0..j)的最长公共子串的长度，注意不包括i和j，前面有一层buffer layer非常重要，就像sputtering那样重要！ f[i][j]=f[i-1][j-1] + 1 when A[i-1]=B[j-1], else f[i][j]=max(f[i-1][j], f[i][j-1])) # 注意有了buffer layer之后，dp中的i对应的是text中的i-1,所以判断条件是when A[i-1]=B[j-1]
- [583. Delete Operation for Two Strings](Solutions/0583.Delete-Operation-for-Two-Strings.py) (M) <br>
f[i][j] = the min number of steps needed to make word1[:i] and word[:j] the same; f[i][j]=f[i-1][j-1] when A[i-1]=B[j-1], else f[i][j]=min(f[i-1][j], f[i][j-1])) + 1
- [0161. One Edit Distance](Solutions/0161.One-Edit-Distance.py) (M) <br>
warm up problem for 72.  One pass solution using two pointers: if s[i] != t[j]: return s[i+1:] == t[j+1:] or s[i+1:] == t[j:] or s[i:] == t[j+1:]
- [0072. Edit Distance/Levenshtein distance](Solutions/0072.Edit-Distance.py) (!!H) <br>
f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离; f[i][j]=min{1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}
- [0097. Interleaving String](Solutions/0097.Interleaving-String.py) (!!H) <br>
f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成; f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)
- [0115. Distinct Subsequences](Solutions/0115.Distinct-Subsequences.py) (H) <br>
dp[i][j] = the number of discinct subeseq until ith char in s and jth char in t; if s[i]!=t[j], dp[i][j] = dp[i - 1][j]  eg: rab, ra; else: rabb, rab, dp[i][j] = dp[i-1][j] + dp[i-1][j-1], 品，细品！ 
- [0044. Wildcard Matching](Solutions/0044.Wildcard-Matching.py) (H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配； 画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"星": if (B[j-1]="?" or A[i-1]=B[j-1]): f[i][j] = f[i-1][j-1]  <br>
情况二：B[j-1]是"星"：可以让"星"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；也可以让"星"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
- [0010. Regular Expression Matching](Solutions/0010.Regular-Expression-Matching.py) (!!H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配; 情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="." or A[i-1]=B[j-1]); 情况二：B[j-1]是"星"：可以让"星"表示0个前面的字符，那就让A[0..i)去和B[0..j-2)匹配： f[i][j] = f[i][j-2]；也可以让"星"表示几个前面的字符，A[i-1]是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j] if (B[j-2]="." or B[j-2]=A[i-1])

--------- 983. Minimum Cost for tickets ---------


### [Other DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M)
- [0718. Maximum Length of Repeated Subarray](Solutions/0718.Maximum-Length-of-Repeated-Subarray.py) (M)
- [1049. Last Stone Weight II](Solutions/1049.Last-Stone-Weight-II.py) (M)
- [1024. Video Stitching](Solutions/1024.Video-Stitching.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0983. Minimum Cost For Tickets](Solutions/0983.Minimum-Cost-For-Tickets.py) (M)
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (M)
- [0361. Bomb Enemy](Solutions/0361.Bomb-Enemy.py) (M)
- [0467. Unique Substrings in Wraparound String](Solutions/0467.Unique-Substrings-in-Wraparound-String.py) (M)
- [0898. Bitwise ORs of Subarrays](Solutions/0898.Bitwise-ORs-of-Subarrays.py) (M)
- [0343. Integer Break](Solutions/0343.Integer-Break.py) (M)
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (M)
- [1105. Filling Bookcase Shelves](Solutions/1105.Filling-Bookcase-Shelves.py) (M)
- [0464. Can I Win](Solutions/0464.Can-I-Win.py) (M)




# [Sliding Window (同向双指针)](/Sliding-window.py)
- [0209. Minimum Size Subarray Sum](Solutions/0209.Minimum-Size-Subarray-Sum.py) (!!M) <br>
维护一个sums, 用来记录i->j中数的和，套模板时满足的条件是sums < target; 更新j: sums += nums[j]; 更新i: sums -= nums[j]
Can we solve in O(NlogN)? Yes, we can traverse the the list, say at i, we search the fisrt j that satisfy sum(nums[i:]>=s), so it is a OOXX probelm, which could be solved using binary search.
- [0003. Longest Substring Without Repeating Characters](Solutions/0003.Longest-Substring-Without-Repeating-Characters.py) (!!M) <br>
维护一个included=set(), 用来记录i->j中include的char，套模板时满足的条件是s[j] not in included; 更新j: included.add(s[j]); 更新i: included.remove(s[i])
- [0076. Minimum Window Substring](Solutions/0076.Minimum-Window-Substring.py) (!!H) <br>
维护一个sourceFreqDict, 用来记录i->j中的char的频率，套用模板时满足的条件是sourceFreqDict all included in targetFreqDict; 更新j: sourceDict[s[j]] += 1, 更新i: sourceDict[s[i]] -= 1.  time complexity is O(MN). solution 2: O(N), instead of using self.allIncluded(sourceDict, targetDict) to check matched or not,  we use a int missing to keep track of how many chars are still needed in order to match, this reduce the time from O(M) to O(1). also, instead of using s[i:j] everytime when we renew res, we use start, end to renew the idx, which reduce time from O(N) to O(1)
It seems there is an O(M+N) solution, same idea of using slideing window, I should understand it later. 山景城一姐有video
- [0340. Longest Substring with At Most K Distinct Characters](Solutions/0340.Longest-Substringwith-At-Most-K-Distinct-Characters.py) (H) <br>
维护一个charDict, 用来记录i->j中的char的频率，套模板时满足的条件是len(charDict) <= k; 更新j: charDict[s[j]+=1; 更新i: charDict[s[i]] -= 1, if charDict[s[i]] == 0: del charDict[s[i]]
- [0713. Subarray Product Less Than K](Solutions/0713.Subarray-Product-Less-Than-K.py) (M) <br>
Note that the numbers are positive, so the prefixProd will be an increasing arr. 维护一个sums, 用来记录i->j中数的product, 指针j再往前跑，指针i在后面追。
- [0242. Valid Anagram](Solutions/0242.Valid-Anagram.py) (E) <br>
string s and t are anagram with each other when all the ch in s have the same count as that in t
- [567. Permutation in String](Solutions/0567.Permutation-in-String.py) (M) <br>
sliding window solution 1: 九章模板，use one collections.Counters for p and one for s. sliding window solution 2: keep the window size len(s1), check the tempCntDict == cntDict ? O(M+M*(N-M)). 
- [0438. Find All Anagrams in a String](Solutions/0438.Find-All-Anagrams-in-a-String.py) (!!M) <br>
similar with 567, 套用九章模板就可以了

------- 
209. Minimum Size Subarray Sum - Medium
159. Longest Substring with At Most Two Distinct Characters - Medium
30. Substring with Concatenation of All Words - Hard
239	Sliding Window Maximum	hard
295	Find Median from Data Stream
228	Summary Ranges	medium
163	Missing Ranges	medium	  ----------



# [Data Structure](/Data-Structure.py)
### [Stack and Queue](/Data-Structure.py)
- [0232. Implement Queue using Stacks](Solutions/0232.Implement-Queue-using-Stacks.py) (E) <br>
use two stack, 要学会写raise IndexError("queue is empty") 的语句
- [0225. Implement Stack using Queues](Solutions/0225.Implement-Stack-using-Queues.py) (E) <br>
use two deques; 要学会抛出error: in pop function, if the stack is empty then raise IndexError("stack is empty");
也可以用一个list实现，每次push进去的时候，把元素插入到最前面即可，与两个queue相比，时间复杂度也还是O(N)
- [0155. Min Stack](Solutions/0155.Min-Stack.py) (!!E) <br>
use two stacks, a stack is to store all items, a minStack to store min items. If a num is less than minStack[-1] then we should append to minStack.
- [0716. Max Stack](Solutions/0716.Max-Stack.py) (E) <br>
Solutino 1: just use one list. Since we have to implement popMax method, we have to find the maxItem pos in the stack, it takes O(N).  Solution 2: by using double linked list and heapq, we can realize O(logN) for push, pop and popMax. Use a doubly linkedlist for popMax.
- [0346. Moving Average from Data Stream](Solutions/0346.Moving-Average-from-Data-Stream.cs) (E) <br>
In C#, Queue class is by default a deque, with two methods: 1. enqueue, meaning push to the back of the queue; 2. dequeue, meaning pop from the front of the queue. They are all O(1).
- [0933. Number of Recent Calls](Solutions/0933.Number-of-Recent-Calls.py) (E) <br>
In C#, Count is a method that gets the number of elements contained in the Queue.
- [0394. Decode String](Solutions/0394.Decode-String.py) (!!M) <br>
定义一个numStack, 一个strStack 存nums和parenthesis. if it's a digit, should use a while loop to add the num in case there are multiple digits; if it's a ch, then put it into strStack; if it's a [, then put the num in numStack and re-initialize the tempNum and tempStr for calculation inside the []; if it's a ], then pop the resStack and signStack and update res.
- [0224. Basic Calculator](Solutions/0224.Basic-Calculator.py) (!!H) <br>
if it's a digit, should use a while loop to add the num in case there are multiple digits, eg: 322 - 16; if it's a sign, then convert to 1 or -1; if it's a (, then append the previous res and sign into the resStack and signStack, and initialize the sign and num for calculation inside the (); if it's a ), then pop the resStack and signStack and update res.
- [0227. Basic Calculator II](Solutions/0227.Basic-Calculator-II.py) (M) <br>
不用stack, 用四根指针prevNum, prevSign, currNum, currSign
---------385	Mini Parser ------ 150	Evaluate Reverse Polish Notation
71	Simplify Path
388	Longest Absolute File Path ---------


### [Iterator](/Data-Structure.py)
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (!!M) <br>
注意这类问题的主程序一般都写在hasNext里面！if topItem.isInteger(): return True; else: if it is a nestedList, 就展开: self.stack = self.stack[:-1] + topItem.getList()[::-1]
- [0251. Flatten 2D Vector](Solutions/0251.Flatten-2D-Vector.py) (M) <br>
Solution 1: use a queue to flatten the 2D vector first. Solution 2: use two pointers, one for row, one for col. O(1) space
- [0281. Zigzag Iterator](Solutions/0281.Zigzag-Iterator.py) (M) <br>
use two pointers and a flag. What if you are given k 1d vectors? How well can your code be extended to such cases? Solution: We append all the list into one deque. Every time we call next(), we pop a list first, then pop the first num from the list, and then re-add it to the end to deque so that we can call it again after k next calls.
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (!M) <br>
saving peeked value in advance
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (!!M) <br>
用stack实现binary search tree的in order traversal的方法类似, 需要额外定义一个 def getLeftMost(self, root)


### [Monotonic stack](/Data-Structure.py) （用于向左/向右寻找第一个比自己大/小的数）
- [0084. Largest Rectangle in Histogram](Solutions/0084.Largest-Rectangle-in-Histogram.py) (!!H) <br>
非单调栈算法：从左向右遍历数组，然后每遍历到一个高度h，向左边找第一个比自己小的的高度在位置i，向右边找第一个比自己小的的高度在位置j，
那此时的面积就是h*(j-i). 这个算法需要向左向右找第一个比自己小的元素，这类问题就要想到用monostack. 通过maintain a monostack,可以很快找到第一个比i小的元素，就是栈中排在i前面的元素，我们需要做的只是向右找了，所以我们向右遍历，每当遇到大于栈顶的值时，直接入栈保持递增stack，如果遇到小于栈顶的值，这时候说明找到了第一个比i（栈顶）小的元素，这时候我们回头且慢莫慌，栈内各个元素依次出栈并回头计算一下面积。
- [0085. Maximal Rectangle](Solutions/0085.Maximal-Rectangle.py) (!!H) <br>
step 1: construct a heights list for each row; step 2: calculate the largestRectangularHistogram of each height using the same method in 84; Should think about dynamic programming solution also.
- [0654. Maximum Binary Tree](Solutions/0654.Maximum-Binary-Tree.py) (M) <br>
solution 1: simple recursionsolution 2: monostack 通过观察发现规律，对于每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的), 维护一个降序数组，可以实现对这个min的快速查找, # O(N), O(N)
- [0496. Next Greater Element I](Solutions/0496.Next-Greater-ElementI.py) (!!M) <br>
scan nums2 from right to left: <br>
for a new scanning item i:  while nums2[i] >= stack[-1]: we pop, until we got a nums2[i]<stack[-1], then this stack[-1] is the next great number we are looking for for nums2[i].  背诵模板！
- [0503. Next Greater Element II](Solutions/0503.Next-Greater-Element-II.py (M) <br>
Double the nums first, then do the same thing as 496.
- [0556. Next Greater Element III](Solutions/0556.Next-Greater-Element-III.py) (M) <br>
very similar with 31. Next Permutation. # step 1: 从右至左找到第一个降序的； # step 2: swap the nums[idx] with the num just larger then it; # step 3: reverse the rest of the list

    
402. Remove K Digits
496. Next Greater Element I (Easy)
503. Next Greater Element II
739. Daily Temperatures
901. Online Stock Span
1130. Minimum Cost Tree From Leaf Values
907. Sum of Subarray Minimums
901. Online Stock Span
856. Score of Parentheses



### [Deque](/Data-Structure.py) 
- [0239. Sliding Window Maximum](Solutions/0239.Sliding-Window-Maximum.py) (H) <br>
heapq的方法是O(NK); deque O(N): Iterate over the array. At each step: I. Clean the deque: 1. Keep only the indexes of elements from the current sliding window; 2. Remove indexes of all elements smaller than the current one, since they will not be the maximum ones. eg: [1,2,7,3,5,4], k = 3, because of 7, 1 and 2 will never be in res; II. Append the current element to the deque. Append deque[0] to the output.


### [Hashmap/Dictionary](/Data-Structure.py) 
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!M youtubed) <br>
use a double linked list and a dictionary; Double linkedlist: newest node append to tail, eldest node remove from head, so that the operation is O(1); Hashmap: key is key, value is the corresponding double linkedlist node
--------LFU!!-------变形题snapchat：在一个data stream 中find top K most frequent number用LFU来解，也可以用heapq NO(k) --
- [0311. Sparse Matrix Multiplication](Solutions/0311.Sparse-Matrix-Multiplication.py) (!!M Facebook) <br>
Sparse matrices, which are common in scientific applications, are matrices in which most elements are zero. To save space and running time it is critical to only store the nonzero elements. Many real world applications of vectors include sparse vectors. An example of it in Machine Learning is the popular one-hot encoding method for categorical computation. We can se a dictinoary to store the index and value of non-zero values, O(M+N + mn), O(M+N), M is the number of elements in matrix A, m is the number of non-zero elements in A.



### [Heap/Heapq](/Data-Structure.py) 
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M) <br>
time: O(NlogK), N 来自于for循环，logK来自于heap的长度是K，heap 的push 和pop都是logK; heapq适合做第K大，第K小，前K大，前K小问题; solution 2: quick select: O(n)
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (M) <br>
需要一个freqDict来记录每个数出现的freq， heapq, heapq中放入的是(freq, key)对; 按照freq来做heapq，这样就保证了可以筛选出most freqent k item; solution 2: quick select should implement; solution 3: bucket sort O(N) faster then solution 2, cuz solution 2 is O(N^2) in worst case.
- [0692. Top K Frequent Words](Solutions/0692.Top-K-Frequent-Words.py) (!!M) <br>
heapq solution: O(N + klogN); quick select solution: O(N + klogk)
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；solution 2: 以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间
- [0973. K Closest Points to Origin](Solutions/0973.K-Closest-Points-to-Origin.py) (M) <br>
（以squre来构建heap就可以了，heap中的元素是(square, point)） quick select is only O(N), I guess all the kth largest problem can use quick select.
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (!!M) <br>
利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。1. use a heap to store (num, row, col); 2. use a set to check if row + 1, col + 1 visited already before push into the heap; Solution 2: binary search 了解一下。<br>
- [0465 Kth Smallest Sum in Two Sorted Arrays](Solutions/0465.Kth-Smallest-Sum-in-Two-Sorted-Arrays.py) (M Lintcode) <br>
将两个list各挑一个数出来的加和做成一个2D Array, 由于两个list都是sorted, 那么这个2D array就是与378同样sorted array了。
- [0023. Merge k Sorted Lists](Solutions/0023.Merge-k-Sorted-Lists.py) (!!M) <br>
maintain一个heapq，初始化将每个list的head放入，然后每次pop出一个最小的，再把最小的那个的.next push进heapq, O(NlogK); we should overriding ListNode compare function __lt__ to make customized compare happens: compare ListNodeSolution 2: divide and conquer, the same as merge sort. O(NlogK)
- [0632. Smallest Range Covering Elements from K Lists](Solutions/0632.Smallest-Range-Covering-Elements-from-K-Lists.py) (!!H) <br>
heapq solution: O(m+nlogm) where m is len(nums), n is len(lst). hq stores (the item in the lst, the lst_idx of where lst is in the nums, the num_idx where the num is in the lst). whenver a min_val is popped, we compare the max_val-min_val with the previous diff. 
Then we push (nums[lst_idx][num_idx+1], lst_idx, num_idx+1) into the heapq and update max_val in the heapq.
- [0621. Task Scheduler](Solutions/0621.Task-Scheduler.py) (!!M) <br>
we only need to be concerned about tasks with higher frequencies. This makes it a perfect candidate for a Priority Queue, or a Max-Heap. 维护一个最大堆 by using negative freq
- [0264. Ugly Number II](Solutions/0264.Ugly-Number-II.py) (M) <br>
维护一个heapq，让它记录从小到大的ugly number, 每次pop出一个currMin，然后生成三个数2* currMin, 3*currMin, 5*currMin, 如果not in seen, 就push进heapq
- [0407. Trapping Rain Water II](Solutions/0407.Trapping-Rain-Water-II.py) (!!H) <br>
Similar with 42. 1D trapping rain water. 1D trapping rain water 是用双指针，一个指针记录左边漏水或储水的可能情况，一个指针记录右边漏水或储水的可能情况。 Step 1: store all the outliners of the matrix in heapq.  Maintain a visited set to mark all the visited locations. Step 2: starting from the min height position, do BFS the 4 possible moves. If found a height < the min Height, then we can store water, else we cannot store water and we should update this leaking point by putting the new height into the heapq
- [0295. Find Median from Data Stream](Solutions/0295.Find-Median-from-Data-Stream.py) (!!H) <br>
定义两个heap: self.leftHq as a maxheap to store the nums that are smaller than median; and self.rightHq as a minheap store the nums that are larger then median.  每次新增一个数num的时候，先根据比 maxheap 中最后一个数大还是小丢到对应的 heap 里。丢完以后，再处理左右两边的平衡性:如果左边太少了，就从右边拿出一个最小的丢到左边。如果右边太少了，从左边拿出一个最大的丢到右边。时间复杂度是O(logN). Follow up questions are important. 
Follow up: leetcode 1093
- [0480. Sliding Window Median](Solutions/0480.Sliding-Window-Median.py) (H) <br>
Solution 1: maitain a sorted window.  We can use binary search for remove and indert. the overall time complexity is O(NK).
similar with 295, we need to maintain two heaps in the window, leftHq and rightHq. To slide one step is actually to do two things: step 1. add a number, which is exactly the same as that in 295. add a number in heapq could be heapq.heappush() which is O(logn) step 2. remove the number that is outside the window; there is not a remmove method in heapq.  We need to implement sift_up and sift_down method for heapq.  Need to implement a heapq in Python!!

----- 313	Super Ugly Number ------- 373	Find K Pairs with Smallest Sums


### [Union-Find](Union-Find-and-Trie.py)
- [0589. Connecting Graph](Solutions/0589.connecting-graph.java) (!!M Lintcode) <br>
将a和b connect: 只需要将a和b的father connect就好；query a和b有没有连接:其实就是判断a和b在不在同一个集合里面，只需要判断find(a) == find(b)
- [0590 Connecting Graph II](Solutions/0590.Connecting-Graph-II.java) (!!M Lintcode) <br>
需要query 点a所在集合的元素个数，所以需要一个list size, 用来记录每个father节点所在集合的点的个数，在union i 和 j 的时候: father[i] = j, sz[j] += sz[i];
- [0591. Connecting Graph III](Solutions/0591.Connecting-Graph-III.py) (!!M Lintcode) <br>
需要query 整个图中有多少个集合，所以需要一个counter, 用来记录图中集合的个数，初始化为n, 在union i 和 j 的时候: father[i] = j, counter--;
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (!!M, youtubed) <br>
Soluiton 1: Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search. <br>
SOlution 2: Union Find: think the grid as a graph, find how may isolated components in the graph, we traversal the whole gird, whenever find a 1, we connect all the 4 adjacent 1s. 方法同lintcode 591.
- [0305. Number of Islands II](Solutions/0305.Number-of-Islands-II.py) (!!H) <br>
Union-Find 算法是解决动态连通性（Dynamic Conectivity）问题的一种算法. 这里的island可以看做是一个图. 每放置一个1, 就将其与其上下左右四个点的1连接起来。O(m×n+L), follow up question?
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
Solution 2: Union find: O(N); Solution 1: BFS O(N)判断图是不是一棵树（不一定非要是二叉树）需要满足两点:1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树
- [0128. Longest Consecutive Sequence](Solutions/0128.Longest-Consecutive-Sequence.py) (!!H) <br>
Solution 1: Greedy O(N) 使用一个集合HashSet存入所有的数字，然后遍历数组中的每个数字，如果其在集合中存在，那么将其移除，然后分别用两个变量pre和next算出其前一个数跟后一个数，然后在集合中循环查找，如果pre在集合中，那么将pre移除集合，然后pre再自减1，直至pre不在集合之中，对next采用同样的方法，
那么next-pre-1就是当前数字的最长连续序列，更新res即可; Solution 2: Union find: O(N)

---------
130 Surrounded Regions 18.6% Medium
547 Friend Circles 49.1% Medium
323 Number of Connected Components in an Undirected Graph 
721 Accounts Merge 
684. Redundant Connection -----------



### [Trie](Union-Find-and-Trie.py)
--- There is a chapter in Leetcode official website for Trie
- [0208. Implement Trie (Prefix Tree)](Solutions/0208.Implement-Trie-(Prefix-Tree).py) (!!M) <br>
Firstly we need to define a TrieNode class, a TrieNode class hs two properties: 1. self.child = collections.defaultdict(TrieNode)  # use a defaultdict, key is char, value is TrieNode corresponding to the char.  2. self.isEnd = False   # return True if reached the end of the Trie.  Then implement 3 methods: insert(word), search(word), startWith(prefix); 注意currNode往下遍历时currNode = currNode.child[char]
- [0211. Add and Search Word - Data structure design](Solutions/0211.Add-and-Search-Word-Data-structure-design.py) (!!M) <br>
addWord mehtod is the same as 208 insert method. But search mehtod is a little different than search method in 208, cuz "." is a wildcard that can represent any char. So we use a queue to store (currNode, idx), then append layer by layer.
- [0212. Word Search II](Solutions/0212.Word-Search-II.py) (!!M) <br>
The capability of finding matching prefix is where the data structure called Trie would shine, comparing the hashset data structure. Not only can Trie tell the membership of a word, but also it can instantly find the words that share a given prefix. 打印所有路径所以用Trie + Backtracking DFS. 非常经典的题呀！
------- 472 ; 677. Map Sum Pairs; 648. Replace Words; 425. Word Squares------------
- [0850. Rectangle Area II](Solutions/ (H) <br>
------- 642. Design Search Autocomplete System -------



# [Breadth First Search](/Breadth-First-Search.py)
### [BFS in Trees](/Breadth-First-Search.py) (总结：Tree中需要一层一层输出的都用BFS)
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (!!M, youtubed) <br>
BFS的铁律就是用queue, 在while q: 循环里做两件事 1. 处理这一层。那就需要把这一层的node逐个pop出，然后append到res里，有时候需要用for循环for _ in range(len(q))来遍历这一层所有的node; 2. append下一层进q。BFS is O(N) since each node is processed exactly once
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (M) <br>
same as 102, 在res.append(level)的时候间隔性选择res.append(level) or res.append(level[::-1])
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (E) <br>
same as 102，只是题目要求从下至上输出，只需要return res[::-1]即可
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (M) <br>
same as 102，只需要res.append(level[-1])即可
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (E) <br>
solution 1: recursion; soluiton 2: BFS; for _ in range(lens): if not node.left and not node.right: return depth
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (!!H) <br>
serialize: just do a bfs to put ch level by level.  deserialize: do a bfs, use an idx to keep track of where have we reached in the input list.
- [0449. Serialize and Deserialize BST](Solutions/0449.Serialize-and-Deserialize-BST.py) (!!H) <br>
Same as 297.  Solution says since BST, the answer could be as compact as possible.  Don't know shy?
- [0652. Find Duplicate Subtrees](Solutions/0652.Find-Duplicate-Subtrees.py) (M) <br>
serialize every root and put into a dictionary, with key is str constructed from the root, val is a list of root that can construct into the root.  Note that in-order traversal never works for serialization!




### [BFS in Graphs](/Breadth-First-Search.py)
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
判断图是不是一棵树（不一定非要是二叉树）需要满足两点:1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M) <br>
Step 1：找到所有的original_nodes，存到一个set里面，用BFS实现; Step 2: 复制所有原有的node，存到mapping中，这样就建立了一个new_node和original_node的一一映射; Step 3: 复制所有original_node对应的neighbors 到 new_node里面
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (!!LintCode) <br>
有向图的问题，可以检测有向图是否有环！必考，其实也非常模板化，一定要记住。Three steps: 1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） (inDegrees = collections.defaultdict(int))，key是node, val是这个node的indegree值; 2. 和每个节点的neighbors （neighbors = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list; 3. 然后 BFS，背诵模板就可以了。
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (!!M) <br>
套用模板分三步：1. collect the inDegree of each node; 2. collect the neighbors information; 3. topological sort - BFS
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (!!M) <br>
套用模板 return res if len(res) == numCourses else []
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (!!M) <br>
这个题目要做三个判断：1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(neighbors) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序; 2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False; 3. 最后判断这个唯一的拓扑排序res是否等于org
- [0269. Alien Dictionary](Solutions/0269.Alien-Dictionary.py) (!!H) <br>
只需要比较word[i]与word[i+1]中每个char，即可得到inDegree的关系以及neighbors的关系



### [BFS in Matrix](/Breadth-First-Search.py) (隐式图搜索问题!!!)
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (!!M, youtubed) <br>
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
Solution 2: dynamic connection problem, Union Find
- [0695. Max Area of Island](Solutions/0695.Max-Area-of-Island.py) (M) <br>
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) <br>
Step 1. append the rotten ones to the first level, Step 2: 层序遍历的bfs to turn the adjacent fresh ones into rotten ones. 必须层序遍历才能保证最少时间make all fresh ones rotten 在class solution(): 后面定义全局变量 EMPTY = 0; FRESH = 1; MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
- [286. Walls and Gates](Solutions/0286.Walls-and-Gates.py) (M) <br>
Step 1: append all the gates into the queue; Step 2: change all the "INF" to a value that equals the layer number, 必须层序遍历才可以保证每次INF都能变成最小距离
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (!!M) <br>
solution 1: 利用对称性质: x,y=abs(x),abs(y); q.append(neighbor) only if (-2 <= next_x <= x + 2 and -2 <= next_y <= y + 2); 1816 ms<br>
solution 2!!!: 从source和destination两端同时进行bfs!!!!注意双端bfs传进去的参数包含q and visited, bfs返回值是updated q and visited. cnt+=1的操作在主函数中进行. while true的结束条件: if visited_src & visited_des: return cnt_src + cnt_des; 452 ms <br>
solution 3: recurrsion with memorization: cache[(x, y)] = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1; 60 ms<br>
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (!!M) <br>
利用双端BFS大大提高速度，注意双端bfs传进去的参数包含q and visited, bfs返回值是updated q and visited. 在双端BFS的过程中判断if not q_src or not q_des: 则说明q_src或q_des里面的所有possible neighbor都不在wordList里面，也就是没有必要继续进行了; The idea behind bidirectional search is to run two simultaneous searches: one forward from the initial state and the other backward from the destination state — hoping that the two searches meet in the middle. The motivation is that b^(d/2) + b^(d/2) is much less than b^d. b is branch number, d is depth. 这题最好定义一个wordSet = set(wordList)来降低时间寻找下一个neighborWord的复杂度到O(26L); 
------ 433. Minimum Genetic Mutation ----------
- [1162. As Far from Land as Possible](Solutions/1162.As-Far-from-Land-as-Possible.py) (M) <br>
bfs: the maximum distance is steps needed to change all WATER to be LAND, so we append all land into the first layer of q, and do a level order bfs. the maxumum distance is then the answer we want. solution 2: DP same as 542. 01 matrix
- [0542. 01 Matrix](Solutions/0542.01-Matrix.py) (M) <br>
方法是先把所有0放入q的第一层，然后一层层遍历，同时更新遇到的1为当前的层数，层数就是1离0的距离; solution 2: DP same as 542. 01 matrix
- [0317. Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (!!H) <br>
Use reachable_cnt[i][j] to record how many times a 0 grid has been reached and use dist[][] to record the sum of distance from all 1 grids to this 0 grid. Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. in the bfs, we do level bfs and update the reachable_cnt matrix and dist matrix. 遇到obstacle不放进q就可以了. each bfs, all position are visited, so O(MNk) where k is how many building are there or how many bfs are triggered. Finnaly return the min of dist[i][j] if reachable_cnt[i][j] = total number of buildings. Strong Prune: if if starting from building (i, j), can reach all other building? if not, that means at least one building is isolated and can not be reached, then return -1 directly: in each BFS we use reachableBuildings to count how many 1s we reached. If reachableBuldings != totalBuildings - 1 then we know not all 1s are connected are we can return -1 immediately, which greatly improved speed.
- [0752. Open the Lock](Solutions/0752.Open-the-Lock.py) (M) <br>
题目蛮有意思的, 带层序遍历的bfs, 遇到currNode in deadends 就不再去访问其neighbor了, find neighbor 函数比较有意思，这里第一次学到了yield;




# [Binary Tree, Divide and Conquer](/Binary-Tree-Divide-and-Conquer.py) <br> 
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) memorize the iterative version using stack
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) memorize the iterative version using stack
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (E) <br>
rootDepth = max(leftDepth, rightDepth) + 1
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (!!E) <br>
for leftPath in leftPaths: rootPaths.append(str(root.val) + "->" + leftPath); 注意递归出口 if not root.left and not root.right: 注意这里往往需要判断之后根节点没有左右节点的特殊的情况，养成好习惯，尤其是本题，没有这个判断无法输出正确结果
- [0112. Path Sum](Solutions/0112.Path-Sum.py) (E) <br>
Similar with 257, find all the paths and put all the pathSums in a set. 
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) <br> 
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
Solution 2: similar with 257 and 112, we just find all the possible paths.
- [0437. Path Sum III](Solutions/0437.Path-Sum-III.py) (M) <br>
不需要从根节点出发，所以 leftCnt_withoutRoot = self.pathSum(root.left, sum); leftCnt_withRoot = self.pathSum(root.left, sum - root.val), why doesnot work?
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) <br>
Divide and Conquer的方法输出以root为根的subTree的subSum，然后每次与minSum打擂台进行比较，注意python中定义全局变量可以用self.minSum = float("inf"), self.minNode = None，在主函数中定义这两个变量就可以了
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) 同上 Divide and Conquer
- [0124. Binary Tree Maximum Path Sum](Solutions/0124.Binary-Tree-Maximum-Path-Sum.py) (H) <br>
题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter. 方法是定义一个self.maxSum在helper函数中去打擂台。helper 函数return the maxPathSum for tree ended with root: return max(left of root, right of root) + root.val; 打擂台: self.maxSum = max(self.maxSum, leftmax + rightMax + root.val)
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) <br>
helper function return (if the tree is balanced, maxDepth); rootIsBalan = leftIsBalan and rightIsBalan and abs(leftMaxDepth - rightMaxDepth) <= 1
- [0543. Diameter of Binary Tree](Solutions/0543.Diameter-of-Binary-Tree.py) (E) <br>
helper function 是 104. Maximum Depth of Binary Tree, 在helper function 中用 self.maxDmtr 去打擂台, self.maxDmtr = max(self.maxDmtr, leftDepth + rightDepth)
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E) <br>
因为是BST, 所以if p.val < root.val < q.val or q.val < root.val < p.val or p.val == root.val or q.val == root.val: return root; Otherwise 要么去左边找要么去右边找。
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (!!M) <br>
- [0250. Count Univalue Subtrees](Solutions/0250.Count-Univalue-Subtrees.py) (M) <br>
从叶子节点出发的方法叫bottum up recurrsion. helper function return if the node is a UnivalTree? 用一个global cnt, 每遇到一个node is a UnivalTree, then cnt += 1.
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E) <br>
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E) <br>
- [0226. Invert Binary Tree](Solutions/0226.Invert-Binary-Tree.py) (E) <br>
STEP 1. divide 先局部有序; STEP 2. conquer 再整体有序
- [0617. Merge Two Binary Trees](Solutions/0617.Merge-Two-Binary-Trees.py) (E) <br>
- [0108. Convert Sorted Array to Binary Search Tree](Solutions/0108.Convert-Sorted-Array-to-Binary-Search-Tree.py) (!!E) <br>
we can always choose the left middle number as root, or always choose right middle number as root, or sometimes left sometimes right as root. That is why the answer is not unique
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M) <br>
注意判断条件不仅仅是left.val<root.val<right.val而是max of left < root < min of right; helper函数返回以root为根的树(是不是BST，max and min value in the tree); if (isLeftBST and isRightBST and maxLeft < root.val < minRight): return True
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (!!M)  <br>
solution 1: 定义两个全局变量self.head, self.curr，进行in order traversal的过程中不断更新curr的位置并hook up nodes
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (M) <br>
divide and conquer: root.right = leftHead; root.left = None; 找到tail并让tail.right = rightHead
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (!!M) <br>
use a stack with controlled recursion, some part of the algorithm is similar with the in order traversal of a tree using a stack; define a getLeftMost function, each time we call next function, we pop the smallestNode from stack and run getLeftMost function for the smallestNode.right if smallestNode.right exist.  this algorithm has space complexity of O(h)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (!!M) <br>
Divide and conquer: if p.val < root.val: return left if left else root; else: return right
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M) <br>
if val > root.val则更新root.right: root.right = self.insertIntoBST(root.right, val); else: root.left = self.insertIntoBST(root.left, val); return root.  这题的recursion exist should be: if not rot: return TreeNode(val). 另外, Time complexity: O(H), where H is a tree height. That results in O(logN) in the average case. So it takes O(logN) to insert an element into a BST.
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (!!M) <br>
Case 1: if node is a leaf, simply delete it Case 2: If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then delete the successor in the right subtree root.right = deleteNode(root.right, root.val). Case 3: If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val). define a function to find successor: find the successor of the root by taking one step right and always left, cuz the successor is the node just larger than the root. define a function to find predecessor: find the predecessor of the root by taking one step left and then always right. Delete a node in BST takes O(logN).
- [1214. Two Sum BSTs](Solutions/1214.Two-Sum-BSTs.py) (M) <br>
Iteratively do an inorder traversal for root1, and store the val in a hashSet; then itteratively do an inorder traversal for root2, and at the same time check if a target-val is in the hashSet. time complexity: O(M + N). 算法跟two sum是一样的，如果闭着眼睛能写要会iterative in-order traversal的哈！
- [1038. Binary Search Tree to Greater Sum Tree](Solutions/1038.Binary-Search-Tree-to-Greater-Sum-Tree.py) (M) <br>
do a in order traversal (reversed version: go all the way to the right) to keep track the addValues
- [0095. Unique Binary Search Trees II](Solutions/0095.Unique-Binary-Search-Trees-II.py) (!!M) <br>
helper(start, end): return the trees from start to end.  Finally return helper(1, n). Time complexity: The main computations are to construct all possible trees with a given root, that is actually Catalan number Gn (超纲).
- [0096. Unique Binary Search Trees](Solutions/0096.Unique-Binary-Search-Trees.py) (M) <br>
same as 95, return len(helper(1, n)).
- [0241. Different Ways to Add Parentheses](Solutions/0241.Different-Ways-to-Add-Parentheses.py) (!!M) <br>
similar with 95, in helper function, return all the different results to add parentheses for input, for i in range(len(input): divide into leftResults and rightResults. Optimization: use a memo dictionary in the helper function to memorize the input that has already been calculated.






# [Depth First Search / Backgracking](/Depth-First-Search.py)
### [Combination](/Depth-First-Search.py)
- [0078. Subsets](Solutions/0078.Subsets.py) (!!M) <br>
C(m, n)：m个里面找出n个的组合问题; 模板的DFS + back tracking求combination问题 O(NS), S是solution的个数，这里S=2^N; 注意两点：1.res.append(curr.copy()); has to be a deep copy; 2. self.dfs(nums, i + 1, curr, res) 要从i+1开始cuz不能回头找会重复
其实可以不用把res传进去，定义一个全局变量self.res即可，可以简化dfs传入的参数。
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (!!M)<br>
如果输入存在重复元素，[1, 2, 2]的遍历中，我们只取前面的那个2，对于后面的那个2，如果不是挨着前面那个2选的，也就是说i != startIndex，那么就不要放后面那个2，这样会造成重复出现[1,第一个2],[1,第二个2], 注意可以挨着第一个2来选第二个2是可以的，因为允许出现[1,2,2]作为答案。所以contraint是: if (i >= 1 and nums[i] == nums[i-1]) and i != startIndex: continue
- [0039. Combination Sum](Solutions/0039.Combination-Sum.py) (M) <br>
模板：find_solution: if target == 0； Is_not_valid：if nums[i] > targetstart是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
- [0040. Combination Sum II](Solutions/0040.Combination-Sum-II.py) (M) <br>
输入中存在重复元素，避免重复输出的方法与Subsets II一样; 模板 find_solution: if target == 0; is_not_valid: if (nums[i] > target) or (i >= 1 and nums[i] == nums[i-1]) and i != startIdx
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (M) <br>
与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解。不理解DP解的for循环顺序。有时间请教高人，怎么理解这个DP的顺序。
- [0216. Combination Sum III](Solutions/0216.Combination-Sum-III.py) (M)<br>
self.dfs(nums, k - 1, n - nums[i], i + 1, curr)   # 不能出现重复数字，所以从i+1开始
- [0090. k Sum II](Solutions/0090.k-Sum-II.py) (M Lintcode) <br>
exactly the same as 216.
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (M)<br>
self.dfs(nums, target - nums[i], 0, curr, res)  # 顺序不重要（(1, 3)和(3, 1)都可以，所以让i从0开始; solution 2: dp. 
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (!!!M) <br>
递归的定义：从s中的start位置开始，挑一些位置切割，判断从start到i的部分是否为回文，如果是就放入curr中，如果i到了string末尾了则说明此事curr是一种组合方式，放入res中 <br>
- [0332. Reconstruct Itinerary](Solutions/0332.Reconstruct-Itinerary.py) (!!M) <br>
有向图的遍历问题，LeetCode关于有向图的题只有两道Course Schedule和Course Schedule II，而那两道是关于有向图的顶点的遍历的，而本题是关于有向图的边的遍历。每张机票都是有向图的一条边，我们需要找出一条经过所有边的路径，那么DFS不是我们的不二选择. Recurssive backtracking.  Worst case: O(E^d), where E is # of edges, d is is the maximum number of flights from an airport.  Solution 2: 因为只需要输出一种包含所有边的路径，所以可以用另一种图的解法 Eulerian Path - every edge is visited exactly once. Eulerian path 使用的算法叫做 Hierholzer algorithm. Hierholzer algorithm 不做backtrack, 所以每一条边只访问一次，所以时间复杂度是O(E), where E is the # of edges.


### [Permutation](/Depth-First-Search.py)
- [0046. Permutations](Solutions/0046.Permutations.py) (!!M)<br>
与combination相比少了一个startIndex参数，加入visited用于防止重复出现; append之后需要将visited[i]变为True; pop出来之后将visited[i]再变回False
- [0022. Generate Parentheses](Solutions/0022.Generate-Parentheses.py) (!!M)  <br>
if leftCnt == n and rightCnt == n: self.res.append(curr) return; if leftCnt < rightCnt: return  # 这个判断尤为关键！
- [0052. N Queens II](Solutions/0052.N-Queens-II.py) (!!H) <br>
排列问题：先打印出数组[0, 1, 2, 3....n]中所有的可能排列：[[0,1,2,3], [1,3,0,2].....]，其中的每一个子数组表示一种可能的方法，子数组中的数字表示在哪个数字的地方放一个Queen，数字对应的下标位置是放那个Queen的行，数字的值是放那个Queen的列。由于Queen可以很冲直撞，所以列是不能相同的，所以需要去重，用visited标记就可以。又由于Queen还可以斜着走，所以横纵坐标的和与差不能相同，也需要用visited标记。用三个字典visited_col, visited_sum, visited_diff分别存储列号，横纵坐标之和，横纵坐标之差有没有被用过
- [0051. N Queens](Solutions/0051.N-Queens.py) (H)<br>
- [0047. Permutations II](Solutions/0047.Permutations-II.py) (M) <br>
模板: is_not_valid: if i in self.visited: continue; if (i > 0 and nums[i] == nums[i-1]) and (i-1) not in self.visited: continue
- [0031. Next Permutation](Solutions/0031.Next-Permutation.py) (M) <br>
step 1: sweeping from right to left, find the first decreasing element nums[i]; Step 2: sweep from right to left, find the first element larger just than nums[i], then swap nums[i] and nums[j], then swap all the items starting from i+1
- [0267. Palindrome Permutation II](Solutions/0267.Palindrome-Permutation-II.py) (!!M)  <br>
step 1: put the characters that have seen two times in the char list; now we have a charList that only holds char that appears even times, eg: "aaaabbc" now becomes "aab", Step 2: we only need to do permutation for this charList, so the time complexity is O((n/2)!), which is quite an improve. Step 3: when return the results, we just use the permuation generated in steps 2 + permuation[::-1]
- [0060. Permutation Sequence](Solutions/0060.Permutation-Sequence.py) (M)  <br>
It really is all about pattern finding; https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
----- 254	Factor Combinations ----



### [树上的DFS](/Depth-First-Search.py) <br>
-------- 979. Distribute Coins in Binary Tree ---------
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) <br> 
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
Solution 2: similar with 257 and 112, we just find all the possible paths.
- [0298. Binary Tree Longest Consecutive Sequence](Solutions/0298.Binary-Tree-Longest-Consecutive-Sequence.py) (!!M) <br> 
Solution 1: 带backtracking the dfs
solution 2: backtracking dfs 的 interative 的写法 by using a stack
Solution 3: 不需要打印所有的路径，所以可以用普通的二叉树的divide and conquer方法：helper function return the Longest Consecutive Sequence **started with** root node, 全局变量res进到helper function中去打擂台
- [0549. Binary Tree Longest Consecutive Sequence II](Solutions/0549.Binary-Tree-Longest-Consecutive-Sequence-II.py) (M) <br> 
Solution 1: divide and conquer方法：helper function return the increasing and decreasing Longest Consecutive Sequence **started with** root node, 全局变量res进到helper function中去打擂台: self.res = max(self.res, root_increasing + root_decreasing - 1)



### [图上的搜索](/Depth-First-Search.py) <br>
- [0093. Restore IP Addresses](Solutions/should solve later) (M)  <br>
根据目前刷了这么多题，得出了两个经验，一是只要遇到字符串的子序列或配准问题首先考虑动态规划DP，二是只要遇到需要求出所有可能情况首先考虑用递归
https://www.cnblogs.com/grandyang/p/4305572.html
- [0017. Letter Combinations of a Phone Number](Solutions/0017.Letter-Combinations-of-a-Phone-Number.py) (!!M) <br>
经典的backtrack题，in dfs template, find solution: if currIdx == len(digits); for next_candidate in list_of_candidates: for ch in self.phone[digits[currIdx]]; is_not_valid: None
- [0079. Word Search](Solutions/0079.Word-Search.py) (!!M) <br>
经典的backtrack题，whenever we find a char == word[0], we trigger a backtracking dfs. in dfs template, find solution:  currIdx == len(word); is_not_valid:  if new_x < 0 or new_x >= len(self.board) or new_y < 0 or new_y >= len(self.board[0]): continue; if (new_x, new_y) in self.visited: continue; if self.board[new_x][new_y] != word[currIdx]: continue; 需要一个visited set来标记已经走过的路径避免走重复的路径。
- [0212. Word Search II](Solutions/0212.Word-Search-II.py) (!!H) <br>
要求打印所有路径所以：Trie + Backtracking DFS. in dfs template, find_solution:  if currNode.isEnd; is_not_valid: if next_x < 0 or next_x >= len(self.board) or next_y < 0 or next_y >= len(self.board[0]): continue; if (next_x, next_y) in self.visited: continue; if self.board[next_x][next_y] not in currNode.child: continue.
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (!!H) 打印/输出所有满足条件的路径必用DFS
Step 1. 从end到start做BFS，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2 <br>
Step 2. 从start到end做DFS，每走一步都必须确保end的distance越来越近(if self.distance[nextWord] >= self.distance[currWord]: continue)。最后将路径都存入到res里
- [0489. Robot Room Cleaner](Solutions/0489. Robot Room Cleaner) (H) 
遍历机器人的四个方向即可，唯一需要注意的是每次都需要调整机器人的朝向才能move一下，毕竟是机器人嘛
- [0037. Sudoku Solver](Solutions/0037.Sudoku-Solver.py) (H) <br> 
dfs + backtracking, time complexity is (9!)^9, which is veyr high. <br>
----------- 980. Unique Paths III ---------- 351. Android Unlock Patterns ---------- 301. Remove Invalid Parentheses ----------- 329. Longest Increasing Path in a Matrix ----------- 1239. Maximum Length of a Concatenated String with Unique Characters ---------- 733. Flood Fill----130. Surrounded Regions------- 417. Pacific Atlantic Water Flow ------ 320. Generalized Abbreviation ----- 753. Cracking the Safe ---- ----- 291	Word Pattern II ---------- 282	Expression Add Operators ------ 140	Word Break II ------ 












# [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (!!E) <br>
九章模板: 1. while start + 1 < end; 2. mid = start + (end - start) // 2; 3. 循环内只写两个分支； 4. 往左逼find the first X; 5. 往右逼find the last X
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) <br>
Find end point using "double method", same as dynamic array
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (E) <br>
两种方法：1. Binary Search; 2. Newton's Method. x<sub>k+1</sub> = (x<sub>k</sub> + x/x<sub>k</sub>) / 2; O(logN) since the set converges quadratically
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (!!M) <br>
用两次二分分别找first pos of target and last pos of target. 想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] **>=** target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。<br>
Follow up: In a sorted array [1,3,4.......], search the elements that are in a certain range eg:[10, 100]. solution: 用两次二分分别找first position of 10 and last position of 100.  Then the elements between the two positions should be in range [10, 100].
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E) <br>
This is to implement bisect.bisect_left(nums, target), which returns the position of inserting target in order to keep nums sorted
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (!!M) <br>
解法一：nums[mid]可以与nums[0]比较；解法二：也可以与nums[-1]比较；解法三：也可以与nums[end]比较
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (H) <br>
与153类似，只是array里可能有duplicates，采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums=[2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2........], 由于不知道mid是1前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N). 这题mid与end比较能work的原因是end永远不可能出现在最小值的左边。
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (M LintCode) <br>
154 相同方法binary search找到minPos, 然后三步反转法recover
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M) 画个图分几个区间讨论就可以了！
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E)<br>
mid 与 mid+1 比较
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M) <br>
OOXX问题，找到第一个出现的X，X是the first position of 递减的序列, mid 要与 mid-1 比较 也要与 mid+1 比较
- [0390. Find Peak Element II](Solutions/0390.Find-Peak-Element-II.java) (H Lintocde) <br>
先二分找到中间某一行的最大值位置(i, j)，然后这个最大值的地方向上(i-1, j)和向下(i-1, j)分别比一下，如果(i, j)最大，那恭喜找到了peak, 如果向上更大，那就往上爬到(i-1,j), 此时i行及其以下的行都可以丢掉了，然后在j那一列查找最大值的位置(ii, j), 这时候在(ii, j)这个位置向左(ii, j-1)向右(ii, j+1)分别比一下，如果发现(ii, j)最大，那么恭喜找到peak了，如果发现(ii, j-1)更大，那就继续往(ii, j-1)爬一步，可以直接丢掉j-1列及其右边的部分了。这样的时间复杂度是T(N)=O(N 在第i行查找最大值)+T(N/2), 所以时间复杂度T(N) = O(N)+O(N/2)+O(N/4)+....+O(2)+O(1) = O(N)+O(N/2)+O(N/4)+....+O(2)+O(1)+O(1)-O(1) = O(2N)-O(1) = O(N).
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) <br>
If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left.
- [0183. Wood Cut](Solutions/0183.Wood-Cut.py) (H Lintcode) <br>
If we can cut into pieces with lens, then we can also cut into prices with len - 1, So this is a OOOXXX problem, to find the last O.
- [0437. Copy Books](Solutions/0437.Copy-Books.py) (!!M Lintcode) <br>
OOOXXX problem, to find the first O. 二分法不难想，难想的是比较mid时的那个helper function, helper function 中 return the least person needed in order to finish all the pages in the midTime.  Algorithm: greedy. 每次发现要超时了就加一个人。 
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) <br>
Think it as a long 1D array with MxN element, then we can use binary search; row = mid // n, col = mid % n; O(log(MN)), O(1)
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) <br>
start from left bottom, head up to right top, each comparism rule out a row (i-1=1) or rule out a col (j+=1). O(M+N).
Comparing with 74, we can see that in 74, the 2D matrix is strongly sorted, so the time is logM + logN <br>
in 240, the 2D matrix is less strongly sorted, so the time is M + N <br>
If hte 2D matrix is not sorted at all, then the time is MN.
- [0050. Pow(x, n)](Solutions/0050.Pow(x,n).py) (M) <br>
recursion solution: half = self.myPow(x, n//2); if n%2 == 0: res = half * half; else: res = half * half * x
- [0029. Divide Two Integers](Solutions/0029.Divide-Two-Integers.py) (M) <br>
eg: 10//3, 每次通过右移3 << 1的方法将3乘以2,这种算法是O(N), 每次都右移几次3 << x, 相当于3x2x2x2...,直到3x2x2x2...>10, 然后取余数继续这个算法
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
SOlution 1: find Kth smallest O(log(M+N)). midIdx1, midIdx2 = len(nums1)//2, len(nums2)//2; midVal1, midVal2 = nums1[midIdx1], nums2[midIdx2]; when k is relatively large, then we can safely drop the first half that are surely smaller than the kth, the question is where is the first half that are surely smaller than the kth? by comparing midVal1 and midVal2, we can find it out, if midVal1 < midVal2, then all the vals in nums1[:midIdx1] are less than midVal2, also all of those vals are less than kth, we can safely drop all those vals






# [Sort](/Sort.py)
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (!!M Youtubed) <br>
quick sort: 用partition function先整体有序，返回pivotPos，然后再pivotPos两边分边局部有序
merge sort: 用mid分成左右两部分，leftArr和righArr分别记录局部的有序数组，然后merge到arr数组
- [0179. Largest Number](Solutions/0179.Largest-Number.py) (M) <br>
quick sort, self-define comparing two strings by: if s1 + s2 <= s2 + s1: return True else False
- [0969. Pancake Sorting](Solutions/0969.Pancake-Sorting.py) (M) <br>
for i in range(lens-1, -1, -1 ): Find maxIndex -> flip max to top -> flip max to bottom of the whole arr -> repeat
- [0280. Wiggle Sort](Solutions/0280.Wiggle-Sort.py) (M) <br>
O(N): 从左到右扫一遍，不满足条件的交换就好了。定义一个变量prevShouldLessThanCurr, in the for loop, prevShouldLessThanCurr = not prevShouldLessThanCurr every step, and based on prevShouldLessThanCurr is true or not, we swap nums[i-1] with nums[i] or not.


### [Partition and quick select](/Sort.py) 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) 
用quick select的模板，partition这个函数的作用是O(N)找到某个数k在一个无序数组中所在的位置，并按照这个数k将该数组分为左右两部分。
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!!M Youtubed)  <br>
solution 1: quick select O(N) in average!!!!; solution 2: heap O(NlogK): heapq.heappush(numsHeap, num); heapq.heappop(numsHeap)
<br> 一个follow up: find the median in a un-sorted array.  solution: this is to find the Kth largest in an array, where K=len(arr)//2
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E) <br>
solution 1: 同向双指针； solution 2: 反向双指针同上题
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
STEP 1: 反向双指针（或同向双指针）对[-1,-2,4,,5,-3,6]进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再正负正负安插
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
solution 1: 做两次partition就可以了; 
solution 2: 同向双指针: move '2's to the right first, then move '1's to the middle
- [0399. Nuts & Bolts Problem](Solutions/0399.Nuts&Bolts-Problem.py) (!!M Lintcode) 
写一个带返回pivotIdx的partition function, 先以nuts[(start+end)//2]为pivotVal对bolts进行partition, 然后返回pivotIdx and pivotVal, 在以这个pivotVal对nuts进行partition, 这样就保证了bolts和nuts进行的是同样的partition; 最后pivotIdx左右两边分别递归调用quickSort function 即可


### [Sorted Array](/Sort.py) 
- [0561. Array Partition I](Solutions/0561.Array-Partition-I.py) (E) <br>
sort the arr first, then the maximum sum of pairs is the sum of every other num
- [0056. Merge Intervals](Solutions/0056.Merge-Intervals.py) (M) <br>
sort the intervals first, res = []; for interval in intervals: if the interval start time is larger than the largest end time in res, then the interval cannot be merged, then res.append(interval), else then res[-1][1] = max(res[-1][1], interval[1])
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
midIdx1, midIdx2 = len(nums1)//2, len(nums2)//2; midVal1, midVal2 = nums1[midIdx1], nums2[midIdx2]; when k is relatively large, then we can safely drop the first half that are surely smaller than the kth, the question is where is the first half that are surely smaller than the kth? by comparing midVal1 and midVal2, we can find it out, if midVal1 < midVal2, then all the vals in nums1[:midIdx1] are less than midVal2, also all of those vals are less than kth, we can safely drop all those vals


### [Bucket Sort](/Sort.py) 
- [0217. Contains Duplicate](Solutions/0217.Contains-Duplicate.py) (E) <br>
hash set to store the seen number, if seen again, return True. Warm up for 219
- [0219. Contains Duplicate II](Solutions/0219.Contains-Duplicate-II.py) (M) <br>
solution 1: dictionary to store the positions where the same num appears. O(N), O(N); solution 2: sliding window: fix the sliding window to be k.  O(N), O(k). Warm up for 220
- [0220. Contains Duplicate III](Solutions/0220.Contains-Duplicate-III.py) (!!M) <br>
Solution 1: brutal force O(n^2); solution 2: Balanced BST O(nlogk); solution 3: bucket method: O(n). bucket sort利用的是分块的思想
The main idea is splitting elements in nums into different buckets in terms of the value of t (for each element, divide by (t+1) for integer division). 保持bucket的大小为t这样只要有两个数被分配到了同一个bucket, 那么就可以return True了
If the result is True, which means one of the following 3 cases hold: 1. Two elements in the same bucket; 2. One in the previous bucket; 3. One in the next bucket. If the case 2 or 3 holds, you need to check if their difference <= t.

--- 451. Sort Characters By Frequency ---



# [Linked List](/Linked-List)
- [0021. Merge Two Sorted Lists](Solutions/0021.Merge-Two-Sorted-Lists.py) (E) <br>
如果需要return一个新的headNode，一般定义一个dummyNode = ListNode(0), curr = dummyNode; 最后return dymmyNode.next
- [0148. Sort List](Solutions/0148.Sort-List.py) (!!M) <br>
step1: divide: 先找到mid, 然后在mid处cut成左右half, 再分别sort left and right; step 2: merge, 同21
- [0206. Reverse Linked List](Solutions/0206.Reverse-Linked-List.py) (!!E) 
需要熟背理解solution 1: interrative, prev, curr = None, head; solution 2: recurssive
- [0092. Reverse Linked List II](Solutions/0092.Reverse-Linked-List-II.py) (M) <br>
reverse node from m to n: step 1: find node_m and node_m_minus; find node_n and node_n_plus; step 2. reverse the nodes from m to n; 3. hook up node_m_minus with node_n, node_m with node_n_plus
- [0024. Swap Nodes in Pairs](Solutions/0024.Swap-Nodes-in-Pairs.py) (M) <br>
Solution 1: recursion, easier to implement. Solution 2: iterative. 想要reverse n1->n2->n3->n4->n5->n6 in pairs: step 1: 在n1前面添加一个dummy n0, 然后在while curr循环里每次都调用reverse函数，reverse函数做的事情是操作四个节点n0->n1->n2->n3, 将其变成n0->n2->n1->n3, 然后return n1，注意每次都是return想要swap的两个节点的前一个节点！step 2: curr = return的n1，然后继续循环
- [0025. Reverse Nodes in k-Group](Solutions/0025.Reverse-Nodes-in-k-Group.py) (!!H) <br>
similar with 24, 在reverse函数中要做的事情是reverse n0->n1->n2------>nk->n_k+1 to be n0->nk------>n2->n1->n_k+1 and return n1; 也是分两步: 首先翻转n1->n2------>nk, 然后hook up n0 with n_k, n1 with n_k+1.  Solution 2: recursion.
- [0141. Linked List Cycle](Solutions/0141.Linked-List-Cycle.py) (E) <br>
在做环形list的题目时,模板是slow, fast = head, head, while fast and fast.next:
- [0142. Linked List Cycle II](Solutions/0142.Linked-List-Cycle-II.py) (!!M) <br>
step 1: 快慢指针找到相遇的点; step 2: 重新定义两根指针p1, p2分别从head和上面相遇的点出发，然后p1,p2相遇的地方就是环的入口
- [0138. Copy List with Random Pointer](Solutions/0138.Copy-List-with-Random-Pointer.py) (!!M) <br>
Solution 1 O(N), O(N): Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, make sure you are not making multiple copies of the same node. we can use extra space to keep old node --> new node mapping to prevent creating multiples copies of same node.   Solution 2 O(N), O(1): use 3 steps, each step requires iterate the loop one time.  step 1: create new node and interleave new node into original node; step 2: link the random pointer for the new nodes; step 3: seperate the interleaved old nodes and new nodes
- [0287. Find the Duplicate Number](Solutions/0287.Find-the-Duplicate-Number.py) (M) <br>
把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。那么如果存在重复的num，那就表示有两个不同node都指向了同一个公共，也就是成环的地点。这么想这个题目就和142一样了，具体实现过程中对p取一个nums[p]，就相当于取一个p.next
- [0160. Intersection of Two Linked Lists](Solutions/0160.Intersection-of-Two-Linked-Lists.py) (E) <br>
两个指针currA, currB; if not currA: currA = headB; if not currB: currB = headA
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (!!M) <br>
本题的考点是关于如何新建一个linked list, 要用someNode.next = ListNode(someVal), 而不是简单的修改value; 还考察了是否细心, 最后很容易漏掉carryBit != 0的判断"
- [0023. Merge k Sorted Lists](Solutions/0023.Merge-k-Sorted-Lists.py) (!!M) <br>
maintain一个heapq，初始化将每个list的head放入，然后每次pop出一个最小的，再把最小的那个的.next push进heapq, O(NlogK); we should overriding ListNode compare function __ lt __ to make customized compare happens: compare ListNode. Solution 2: divide and conquer, O(NlogK), should also understand.



# [SubArray](/SubArray.py)
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (!!E) <br>
Maintian a prefixSum and minPrefixSum, so that maxSubSum = max(maxSubSum, prefixSum - minPrefixSum); minPrefixSum = min(prefixSum, minPrefixSum)
- [0724. Find Pivot Index](Solutions/0724.Find-Pivot-Index.py) (E) <br>
在nums前面添加一个[0]然后再进入循环。for i, num in enumerate([0] + nums[:-1]): if prefixSum * 2 == sumNums - nums[i]: return i
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M) <br>
新建一个prefixSumDict = {0: 1}, key是prefixSum, val是how many times the prefixSum appears; if prefixSum - k in prefixSumDict: 等价于if prefixSum[j+1]-prefixSum[i] == k
- [1074. Number of Submatrices That Sum to Target](Solutions/1074.Number-of-Submatrices-That-Sum-to-Target.py) (H) <br>
也可以先把行处理好，让每一行里面保存上面所有行的和，接下来就是在每一行里面去求560问题了，注意一点不同的是需要遍历upRow和downRow的, 如果不遍历就是solution 3的错误写法举一个反例想明白solution 3为什么行不通，自然就会改成solution 2了O(MMN)
- [0523. Continuous Subarray Sum](Solutions/0523.Continuous-Subarray-Sum.py) (M) <br>
prefixSumMap = {0: -1} # key: prefixSum[j], val: j/position, initial position should be -1; prefixSum += num; prefixSum = prefixSum % k 因为题目要求要能被subArray Sum 要能被k整除
- [0974. Subarray Sums Divisible by K](Solutions/0974.Subarray-Sums-Divisible-by-K.py) (M) <br>
prefixSumDict = {0: 1} # key is the prefixSum, val is how many times the prefixSum appears; prefixSum += num; prefixSum %= K
- [0139. Subarray Sum Closest](Solutions/0139.Subarray-Sum-Closest.py) (M Lintcode) <br>
题目要求NlogN, 那就是疯狂暗示要sort, prefixSumList = [(0, -1)] # (0, -1) are prefixSum and index; 对prefixSum来进行sort，这样最小的subArrSum (或者prefixSums[j+1][0] - prefixSums[i][0])就一定来自于相邻的两个prefisxSums了
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (M) <br>
最大值问题。用一个数组记录最大的正数maxDP[i]，另一个数组记录最小的负数minDP[i], maxDP[i]表示以i为结尾的subarray的最product. 分nums[i]的正负,更新maxDP[i]和minDP[i]。maxDP[i] = max(nums[i], maxDP[i-1]* nums[i]) if nums[i]>0






# [Two Pointers](/Two-pointers.py)
### [反向双指针](/Two-pointers.py)
- [0977. Squares of a Sorted Array](Solutions/0977.Squares-of-a-Sorted-Array.py) (E) <br>
three pointers: i starts from beginning of A; j starts from the end of A; k starts from end of res 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) 
用quick select的模板，partition这个函数的作用是O(N)找到某个数k在一个无序数组中所在的位置，并按照这个数k将该数组分为左右两部分。
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E) <br>
solution 1: 同上31的方法做partition; solution 2: 同向双指针: anchor and curr, swap A[anchor] and A[curr] when A[curr] is even
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
STEP 1: 反向双指针进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再来进行正负正负正负安插
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
solution 1: typical partition problem, step 1: 先把0放到最前面; step 2: 再把2放到最后
solution 2: 同向双指针的方法也应该理解掌握！
- [0238. Product of Array Except Self](Solutions/0238.Product-of-Array-Except-Self.py) (M) <br>
定义两个数组分别记录product before ith num: fwd[i]=fwd[i-1] * nums[i-1] and product after ith num: bwd[i]=bwd[i+1] * nums[i+1], then res[i]=fwd[i] * bwd[i]
- [0011. Container With Most Water](Solutions/0011.Container-With-Most-Water.py) (!!M) <br>
if height[i] > height[j]: j -= 1  # meaning that 右边的栅栏更低，所以把右边指针移动一下，希望能用长度去compromise宽度，即寄希望于min(height[i], height[j])会变大，来compromise掉(j - i)的变小. 为什么不移左边指针呢？因为移动左边的话，min(height[i], height[j])不会变大，但是(j - i)一定变小，所以面积一定变小.


### [同向双指针](/Two-pointers.py)
- [0415. Add Strings](Solutions/0415.Add-Strings.py) (E) <br>
similar with leetcode 2.  while i >= 0 and j >= 0:  循环之后，还要check while i >= 0: ;  while i >= 0: ; 最后还要check if carryBit > 0:
- [0019. Remove Nth Node From End of List](Solutions/0019.Remove-Nth-Node-From-End-of-List.py) (M) <br>
fast 比 slow 先出发 n 步即可
- [0088. Merge Sorted Array](Solutions/0088.Merge-Sorted-Array.py) (E) <br>
modify nums1 in-place, 由于nums1有足够空间，我们可以从nums1的尾部开始排，use i, j, k = m - 1, n - 1, m + n -1; 把最大的数放到nums1的后面
- [0283. Move Zeroes](Solutions/0283.Move-Zeroes.py) <br>
anchor is the first zero element, __anchor keeps all the non-zero numbers on it's left, that is the reason the pointer is called anchor__. while curr runs forward, whenever curr equals a non-zero number, switch it to anchor, and move anchor one step forward.  Solution 2: partition using the method in 31, but not accepted cuz partition changes the original order of non-zero numbers
- [0026. Remove Duplicates from Sorted Array](Solutions/0026.Remove-Duplicates-from-Sorted-Array.py) (!!E) <br>
典型的同向双指针 on the left of anchor (including anchor) are the maintained array without duplicates
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) <br>
同向双指针法，注意题目需要去重，如果碰到符合条件的，把i和j往前挪到不重复的元素去。
- [0042. Trapping Rain Water](Solutions/0042.Trapping-Rain-Water.py) (!!H) <br>
首先找到最高highestBar的位置。然后从左边往最高的位置扫，同时maintain一个指针记录leftHighest的高度，如果扫到的地方i小于这个leftHighest的高度，
则说明i这个地方可以蓄水，可蓄水量为leftHighest的高度减去i的高度；如果扫到的地方i大于这个leftHighest的高度，则说明i这个地方不可以蓄水，所以这时候要更新leftHighest为i的高度。同理对右边做同样的操作



# [Two Sum]()
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (E) <br>
九章算法：对于求 2 个变量如何组合的问题可以循环其中一个变量，然后研究另外一个变量如何变化, 普世的方法是：for循环一个变量a，然后看另外一个变量target-a是不是在一个hashmap中
- [0167. Two Sum II - Input array is sorted](Solutions/0167.Two-Sum-II-Input-array-is-sorted.py) (E) <br>
sorted 就用反向双指针
- [0170. Two Sum III - Data structure design](Solutions/0170.Two-Sum-III-Data-structure-design.py) (E) <br>
self.numsDict = collections.defaultdict(lambda: 0) # val is num val, key is how namy times the val was added
- [0653. Two Sum IV - Input is a BST](Solutions/0653.Two-Sum-IV-Input-is-a-BST.py) (E) <br>
In order traversal into an array and then use two pointer method
- [1099. Two Sum Less Than K](Solutions/1099.Two-Sum-Less-Than-K.py) (E) <br>
最优解是sort之后用反向双指针O(nlogn); solution 2: bucket sort: O(n)? coudl be a good follow up question.
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) <br>
同向双指针法，注意题目需要去重，如果碰到符合条件的，把i和j往前挪到不重复的元素去。
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (E) <br>
if nums[i] + nums[j] <= target: cnt += j - i		# 注意这里是 cnt += j - i 表示nums[i] 加上 i 到 j之间的任何数，一定也是小于等于target的
- [1214. Two Sum BSTs](Solutions/1214.Two-Sum-BSTs.py) (M) <br>
Iteratively do an inorder traversal for root1, and store the val in a hashSet; then itteratively do an inorder traversal for root2, and at the same time check if a target-val is in the hashSet. time complexity: O(M + N). 算法跟two sum是一样的，如果闭着眼睛能写要会iterative in-order traversal的哈！
- [0015. 3Sum](Solutions/0015.3Sum.py) (!!M) <br>
step 1: sort the list; step 2: 背模板，注意点一：对i去重；注意点二：left, right=i+1, lens-1; 注意点三：left和right的初始值；注意点三：对left和right去重
- [0016. 3Sum Closest](Solutions/0016.3Sum-Closest.py) (M) <br>
- [0259. 3Sum Smaller](Solutions/0259.3Sum-Smaller.py) (M) <br>
优化：if nums[i] * 3 >= target: break；解法类似609
- [0018. 4Sum](Solutions/0018.4Sum.py) (M) <br>
solution 1: O(N^3): 3Sum模板双指针法。注意这里给j去重不能从j>=1开始，因为要至少让j先取上第一个值i+1之后才能与前一个数比较！不然[0,0,0,0], 0就通不过了；solution 2: O(N^2): hashmap. for循环a, b,保存a+b的值进hashmap, 再for循环c, d, 判断c+d是否在hashmap中
- [0454. 4Sum II](Solutions/0454.4Sum-II.py) (M) <br>
有四个数组，不好用双指针，所以就使用hashmap，用一个hashmap 保存a + b
- [0089. k Sum](Solutions/0089.k-Sum.py) (H Lintcode) <br>
采用动态规划，用dp[i][j][t]表示前i个数里选j个和为t的方案数。dp[i][j][t] = 选A[i-1]: dp[i-1][j-1][t-A[i-1]] + 不选 A[i-1]: dp[i-1][j][t]; initialize: dp[i][0][0] = 1; return dp[lens][k][target]




# [Sweep-Line](/Sweep-Line.py) <br>
- [0391. Number of Airplanes in the Sky](Solutions/0391.Number-of-Airplanes-in-the-Sky.py) (M Lintcode) <br>
扫描线做法：碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。
Step 1: 我们分别把所有的start和所有的end放进两个数组，并排序。Step 2: 然后从第一个start开始统计，碰到start较小就加一，碰到end较小就减一。并且同时维护一个最大飞机数的max。
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；minimum meeting rooms required could be understood us maximum meeting rooms in use
Then this problem is exaclty the same as the lintcode 0391. Number of Airplanes in the Sky <br> solution 2: 先把interval进行sort: intervals.sort(key = lambda x: (x[0], x[1])), 然后以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间
- [0218. The Skyline Problem](Solutions/0218.The-Skyline-Problem.py) (!!H) <br>
sweep lint + heapq；a maxHeap to store all alive buildings, 存高度和终点. res 里面需要保存的其实是每一次高度发生变化时的终点. 在指针currPos做扫描的时候做三件事情: 1. pop buildings that end before curPos, cuz they are no longer "alive"; 2. push [negative_height, end_point] of all buildings that start before curPos; 3. 更新res: if -maxHeap[0][0] != prevHeight: 说明出现了一个拐点要么上升要么下降，这时候就需要append拐点了





# [Greedy](/) <br>
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!M) <br>
存在性问题。状态: dp[j]=能不能跳到位置j; 转移方程：dp[j]=True if dp[i] and nums[i]>=j-i) (TLE 注意只要有一个dp[i]是的dp[j]=True了就可以break了). DP解法: O(N^2).  Greedy 解法: O(N) Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index (currPosition + nums[currPosition] >= leftmostGoodIndex). 
If we can reach a GOOD index, then our position is itself GOOD. Iteration continues until the beginning of the array. 
If first position is a GOOD index then we can reach the last index from the first position.
- [0045. Jump Game II](Solutions/0045.Jump-Game-II.py) (H) <br>
Greedy算法：第一步可以跳到比如位置10，也就是说0-10我们都可以一步跳到，那我们就在0-10这些位置中，选一个位置i跳第二步，看看第二步能跳到最远的地方是哪里，比如是最远的是从位置6跳到位置28，那么就说明两步可以跳到位置28，也就是说11-28我们可以通过两步跳到，那我们就继续在11-28这些位置中，选一个位置i跳第三步.........
- [1306. Jump Game III](Solutions/1306.Jump-Game-III.py) (M) <br>
BFS, if can find arr[idx]==0, then return True.
1024. 视频拼接，中等
1326. 灌溉花园的最少水龙头数目，困难







# [系列题](/)
##  [Intervals](/)
------ 252 meeting room[easy] ------
------- 56	Merge Intervals; 57	Insert Interval --------
--------- 352	Data Stream as Disjoint Intervals --------
- [1229. Meeting Scheduler](Solutions/1229.Meeting-Scheduler.py) (M) <br>
双指针法, if min(end1, end2) - max(start1, start2) >= duration: return [max(start1, start2), max(start1, start2) + duration]
- [0391. Number of Airplanes in the Sky](Solutions/0391.Number-of-Airplanes-in-the-Sky.py) (M Lintcode) <br>
扫描线做法：碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。
Step 1: 我们分别把所有的start和所有的end放进两个数组，并排序。Step 2: 然后从第一个start开始统计，碰到start较小就加一，碰到end较小就减一。并且同时维护一个最大飞机数的max。
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；minimum meeting rooms required could be understood us maximum meeting rooms in use
Then this problem is exaclty the same as the lintcode 0391. Number of Airplanes in the Sky <br> solution 2: 先把interval进行sort: intervals.sort(key = lambda x: (x[0], x[1])), 然后以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间



## [Perfect Rectangle](/)
- [0836. Rectangle Overlap](Solutions/0836.Rectangle-Overlap.py) (E) <br>
比较点的坐标即可
- [0223. Rectangle Area](Solutions/0223.Rectangle-Area.py) (M) <br>
分成是否overlap两种情况来计算
- [0391. Perfect Rectangle](Solutions/0391.Perfect-Rectangle.py) (H) <br>
属于观察题目性质的题, In order to form a perfect rectangle, two condictions must be satisfied:
condition 1. for all the coordinates, there are 4 and only 4 coordinates that appear only once, others appear either twice or 4 times.  So we can use a set to store all the coordinates and cnt their appear times
condition 2. the sum of area of all the small rectangles should be the same as the whole big one (the area enclosed by the 4 coordinates in condition 1)




# [图的遍历](/)
## [图的基础](/)
----- 0547.friend-circles --------
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M) <br>
Step 1：找到所有的original_nodes，存到一个set里面，用BFS实现; Step 2: 复制所有原有的node，存到mapping中，这样就建立了一个new_node和original_node的一一映射; Step 3: 复制所有original_node对应的neighbors 到 new_node里面
- [0399. Evaluate Division](Solutions/0399.Evaluate-Division.py) (!!M) <br>
Solution 1: bfs 去做path compression
注意这里构建图的时候采用hashmap构建邻接表 graph = collections.defaultdict(dict)  
in graph, key is node1, val is a dict of (key: node2, val: node1/node2)
Given the number of variables N, and number of equations E,
building the graph takes O(E), each query takes O(N), space for graph takes O(E)
I think if we start to compress paths, the graph will grow to O(N^2) gradually, and we can optimize each query to O(1), 
that is why we use global variable for graph, so that we can compress paths and avoid duplicated computing;  Soltution 2: Union Find;  Solution 3: Floyd–Warshall algorithm
- [0310. Minimum Height Trees](Solutions/0310.Minimum-Height-Trees.py) (M) <br>
想想如果是一个很大的图，那minimum height trees的root就应该是这个图的最中心，所以我们就去找图的最中心就可以了，采用从外围(inDegree=1的node)往中间走的方法，解法类似topological sort, 走到最后留下的顶点就是最中心的顶点，也就是距离所有外围顶点最小的顶点。
## [Celebrity](/)
- [0997. Find the Town Judge](Solutions/0997.Find-the-Town-Judge.py) (E) <br>
one dict to store the inDegree (beingTrusted), one dict to store the outDegree (trustOthers). there exsit a town judge only if there is a node with inDegree==N-1(beiing trusted by all others), and at the same time the node should have outDegree==0(not trust anyone)
- [0277. Find the Celebrity](Solutions/0277.Find-the-Celebrity.py) (!!M) <br>
main algorithm: each comparing kowns(i, j), we are sure either i is definitely not a celebrity (knows(i, j)=True), or j is definitely not a celebrity (knows(i, j)=False). step 1: one pass, find a candidate by making sure other people are not candidates; step 2: one pass, double check the candidate selected in step 1 is indeed a celebrity

## [Dijkstra](/)
- [0743. Network Delay Time](Solutions/0743.Network-Delay-Time.py) (!!M) <br>
**带权值**的**有向图**求**单源节点**出发的最短路径问题马上就想到Dijkstra, **O(NlogN + E)** N is # nodes, E is # edges <br>
Dijkstra就是贪心版的bfs, bfs是勤勤恳恳一层一层推进，一层没访问完绝不访问下一层。Dijkstra就很贪心了，才不一层一层地走呢，他每次都想走最low cost的。如何实现每次走最low cost的呢？用一个heapq来store a pair: (currCost to reach the node, node), 这样每次pop出来的就都最low cost的node了，再去访问这个node的neighbors，把这些neighbors都加到hq中，代码比较短。思路其实与23. Merge k Sorted Lists非常类似，把23里的linked list加上一个虚拟头节点连接所有的头节点，然后把Linked list node的val改成边的权值，那就变成了单源节点出发求访问到所有节点的最短路径。
- [0787. Cheapest Flights Within K Stops](Solutions/0787.Cheapest-Flights-Within-K-Stops.py) (!!M) <br>
有向图，带权值，找从单源出发最佳路径问题：Dijkstra's algorithm O(NlogN + E) <br> 
hq 需要 store (cost, stops, airports), 与743相比少了一个currNode in costs: continue因为次好路径也可能是最后的结果，这是由于最好路径可能不满足stops < K; 这题需要加一个 if currStops >= K: continue
- [0882. Reachable Nodes In Subdivided Graph](Solutions/0882.Reachable-Nodes-In-Subdivided-Graph.py) (M) <br>
hq store (how many moves left, node); # seen[i] means that we can arrive at node i and have seen[i] moves left; if movesLeft > insertNumber: heappush

## [A*](/)
- [1091. Shortest Path in Binary Matrix](Solutions/1091.Shortest-Path-in-Binary-Matrix.py) (M) <br>
solution 1: 带层序遍历的bfs, if grid[next_x][next_y] == BLOCK 那就continue掉不放进q; solution 2: bi-directional bfs; solution 3: A*, **A* is better than bfs in finding the shorted path from source node to end node.** 这是一道经典的A* 题，很有启发性，以后做完一道bfs求最短路径的题，都可以想想能不能用A-star的方法求解，只要可以想到可行的heuristic estimation的方法，都可以尝试将bfs改成更快的A* . bfs 需要visit every node. but A* only greedily choose the best route to go. The best route is estimated by heuristic estimation. 在A* 算法中，heuristic estimation 一定要入队列进行排序，而且当前的steps也要入队列，heapq stores (1. heuristic estimation of min # of steps from source to target if 经过currNode, 2. currNode_pos, 3. steps from source to currNode)
- [1263. Minimum Moves to Move a Box to Their Target Location](Solutions/1263.Minimum-Moves-to-Move-a-Box-to-Their-Target-Location.py) (H) <br>
思路：这个题是从源节点到目标节点的最短路径问题，所以想到用bfs, 源节点是对boxPos, 目标节点是targetPos, 从源节点出发做带层序遍历的bfs_1, return 层数即可。注意在判断nextBoxPos是否可以append到q的时候需要兼顾考虑到player能不能到nextBoxPos的相反方向去推box, 所以需要找到从currPlayerPos到oppositeNextBoxPos的可能路径，这是一个从源节点到目标节点的问题，源节点是对currPlayerPos, 目标节点是oppositeNextBoxPos, 需要做bfs_2, 如果能到就返回true. 总体思路就是上述了，需要注意的是bfs_1中由于box每移动一下boxPos会变playerPos也会变，所以要把boxPos和playerPos都入队列。另外易错点：visited里面只装boxPos. 这是不对的, 因为box从不同的方向被推到同一个地方是允许的，因此visited里面应该装入(boxPos, the pos where the boxPos comes from). <br>
SOlution 2: 无权图单源节点的最短路径问题，自然想到A-star search algorithm. use manhatan distance as Heuristic esitimation for A-star algorithm: steps + (abs(nextBoxPos[0]-targetPos[0]) + abs(nextBoxPos[1]-targetPos[1])).  put the heuristic estimation in the hq, together with steps, so the hq stores (heristic estimation of hte minimum steps needed from source to target, steps, boxPos, playerPos).  in A* algorithm, do not do level order bfs, do non-level order bfs.  







## 抓大放小，下面的算法可以先不去管！
#### [Floyd-Warshall](/)
#### [Bellman-Ford](/)
- [0743. Network Delay Time] 花花酱
#### [Kruskal/Prim](/)
1135. Connecting Cities With Minimum Cost; Eddie 讲的课
#### [Tarjan's](/)
1192. Critical Connections in a Network


## [Advanced Trees](/)
#### [Red/Black tree](/)
#### [Splay tree](/)
#### [AVL tree](/)
#### [Morris 线索二叉树](/)
#### [Fenwick tree](/)
-----   315. Count of Smaller Numbers After Self ----------






# [Random](/)
384	Shuffle an Array	视频讲解	
398	Random Pick Index	视频讲解	
382	Linked List Random Node	视频讲解	
380	Insert Delete GetRandom O(1)	视频讲解	
381	Insert Delete GetRandom O(1) - Duplicates allowed	视频讲解	
138	Copy List with Random Pointer	视频讲解



# [Desgin](/)
359	Logger Rate Limiter	视频讲解	
346	Moving Average from Data Stream	视频讲解	Sliding Window
362	Design Hit Counter	视频讲解	
281	Zigzag Iterator	视频讲解	
284	Peeking Iterator	视频讲解	
251	Flatten 2D Vector	视频讲解	
288	Unique Word Abbreviation	视频讲解	
170	Two Sum III - Data structure design	视频讲解	
348	Design Tic-Tac-Toe	视频讲解	
379	Design Phone Directory	视频讲解	
353	Design Snake Game	视频讲解	
146	LRU Cache	视频讲解	
355	Design Twitter	视频讲解	
303	Range Sum Query - Immutable	视频讲解	
304	Range Sum Query 2D - Immutable	视频讲解	
307	Range Sum Query - Mutable	视频讲解	BIT & ST
308	Range Sum Query 2D - Mutable	视频讲解	BIT & ST
460. LFU Cache
588. Design In-Memory File System
604. Design Compressed String Iterator






# [Company High Freq](/)
## [Google](/)
Count Complete Tree Nodes; Longest Increasing Path in a Matrix; Evaluate Division; Cracking the Safe; Robot Room Cleaner; Most Stones Removed with Same Row or Column; Flip Equivalent Binary Trees; Word Squares; Count of Smaller Numbers After Self; Peak Index in a Mountain Array; Split Array Largest Sum; Logger Rate Limiter; Insert Delete GetRandom O(1); Design Search Autocomplete System; Reverse Integer; Candy; Isomorphic Strings; Strobogrammatic Number; Bulls and Cows; Range Sum Query 2D - Mutable; My Calendar II; Jewels and Stones; Swap Adjacent in LR String; Guess the Word; Minimum Area Rectangle














# Other Algorithms
### [Rabin Karp / Rolling Hash]()
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (E) (Rabin Karp Algorithm O(M+N), use Hashcode, ord(ch)-ord("a"))
1062. Logest repeating substring







## Let's take a look at the famous Algorithm book.
### top 50 of interview questions and top liked questions and top Google interview questions top green
## 把laioffer视频里的题都刷一遍！
## 九章高频
## 九章Python
