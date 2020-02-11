
## [Dynamic Programming](Dynamic-Programming.py)
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (M) (最小值问题。状态: f[X]=最少用多少枚硬币拼出X; f[X] = min{f[X-2]+1, f[X-5]+1, f[X-7]+1})
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (M) (存在性问题。状态: dp[j]=能不能跳到位置j; dp[j]=True if dp[i] and i+nums[i]>=j) (TLE)
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (M) (最大值问题。用一个数组记录最大的正数，另一个数组记录最小的负数, maxDP[i] = max(nums[i], maxDP[i-1]*nums[i])) if nums[i]>0

### [坐标型DP](/Dynamic-Programming.py)
- [0062. Unique Paths](Solutions/0062.Unique-Paths.py) (!!M) (状态: f[i][j]=有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = f[i][j-1]+f[i-1][j])
- [0063. Unique Paths II](Solutions/0063.Unique-Paths-II.py) (M) (状态: f[i][j]=f[i][j]为机器人有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = 0 if it is obstacle else f[i][j-1]+f[i-1][j])
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (!!M) (滚动数组做空间优化)
- [0120. Triangle](Solutions/0120.Triangle.py) (M) (滚动数组做空间优化)


### [序列型DP](/Dynamic-Programming.py)
- [0256. Paint House](Solutions/0256.Paint-House.py) (E) 
265 (时间优化：记录最小值和次小值min_1, min_2的position j_1和j_2)
198 （空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]）
213 （与House robber I 相比，这个题目的房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：
1. 房子1没偷：问题变成了对房子2~N做House robber I的问题
2. 房子N没偷：问题变成了对房子1~N-1做House robber I的问题）
#### [Buy and sell stock]()
121
122
123
188
309 （状态很多很难理清楚的时候使用状态机很有效）（直播）
714
####  [最长序列问题](/Dynamic-Programming.py)
- [0674. Longest Continuous Increasing Subsequence](Solutions/0674.Longest-Continuous-Increasing-Subsequence.py) (E) 
300 (!!M)
673
354
334


###  [划分型DP](/Dynamic-Programming.py)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M) 
279  （f[j] = min(f[j-i^2]+1) for i^2<=j）
132   （f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome）
473 (M Lintcode) 


### [博弈型DP](/Dynamic-Programming.py)
394 Lintcode

### [背包型DP](/Dynamic-Programming.py)
92 lintcode f[i][m]=能否用前i个物品拼出重量m。f[i][m] = f[i-1][m] or f[i-1][m-A[i-1]]
563 lintcode f[i][m]=前i个物品能拼出重量m有多少种方式。f[i][m] = f[i-1][m] + f[i-1][m-A[i-1]]
377 f[i]=how many ways to combine to number i  背包问题一定要把总承重放到状态里！！ f[i]=f[i-A1]+f[i-A2]+f[i-A3]....



### [位操作型DP](/Dynamic-Programming.py)
- [0338. Counting Bits](Solutions/0338.Counting-Bits.py) (M) (dp[i] = dp[i >> 1] + i % 2 )


### [Longest Subsequece Problems](/Longest-Subsequece-Problem.py)
- [0005. Longest Palindromic Substring](Solutions/0005.LongestPalindromicSubstring.py) (Center spread O(N^2); DP(N^2))
- [0516. Longest Palindromic Subsequence](Solutions/0516.LongestPalindromicSubsequence.py) (M)
- [0300. Longest Increasing Subsequence](Solutions/0300.LongestIncreasingSubsequence.py) (M)
- [0673. Number of Longest Increasing Subsequence.py](Solutions/0673.NumberofLongestIncreasingSubsequence.py) (M)
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.LongestArithmeticSequence.py) (M)
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.LengthofLongestFibonacciSubsequence.py) (M)  
### [高频 DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M)
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (M)
- [0718. Maximum Length of Repeated Subarray](Solutions/0718.Maximum-Length-of-Repeated-Subarray.py) (M)
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M)
- [1049. Last Stone Weight II](Solutions/1049.Last-Stone-Weight-II.py) (M)

- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M)
- [1024. Video Stitching](Solutions/1024.Video-Stitching.py) (M)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (M)
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M)
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M)
- [0983. Minimum Cost For Tickets](Solutions/0983.Minimum-Cost-For-Tickets.py) (M)
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0361. Bomb Enemy](Solutions/0361.Bomb-Enemy.py) (M)
- [0464. Can I Win](Solutions/0464.Can-I-Win.py) (M)
- [0467. Unique Substrings in Wraparound String](Solutions/0467.Unique-Substrings-in-Wraparound-String.py) (M)
- [0898. Bitwise ORs of Subarrays](Solutions/0898.Bitwise-ORs-of-Subarrays.py) (M)
- [0343. Integer Break](Solutions/0343.Integer-Break.py) (M)
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (M)
- [1105. Filling Bookcase Shelves](Solutions/1105.Filling-Bookcase-Shelves.py) (M)




## [Data Structure](/Data-Structure.py)
### [Stack and Queue](/Data-Structure.py)
- [0232. Implement Queue using Stacks](Solutions/0232.Implement-Queue-using-Stacks.py) (E) 
- [0225. Implement Stack using Queues](Solutions/0225.Implement-Stack-using-Queues.py) (E) 
- [0155. Min Stack](Solutions/0155.Min-Stack.py) (!!E) 
- [0716 (没搞懂！)] (E) 
- [0394. Decode String](Solutions/0394.Decode-String.py) (M) 
#### [Iterator](/Data-Structure.py)
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (M) 
- [0251. Flatten 2D Vector](Solutions/0251.Flatten-2D-Vector.py) (M)
- [0281. Zigzag Iterator](Solutions/0281.Zigzag-Iterator.py) (M)
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (M)
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M)
#### [单调栈](/Data-Structure.py)
84. Largest Rectangle in Histogram  (H) (should understand later)


### [Hashmap/Dictionary](/Data-Structure.py)
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!M)


### [Heap/Heapq](/Data-Structure.py)
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M)
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (M)
- [0253. Meeting Rooms II](Solutions/00253.Meeting-Rooms-II.py) (!!M) (以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间)
- [0973. K Closest Points to Origin](Solutions/0973.K-Closest-Points-to-Origin.py) (M) （以squre来构建heap就可以了，heap中的元素是(square, point)）
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (M)
- [0264. Ugly Number II](Solutions/0264.Ugly-Number-II.py) (M)


## [Two Sum]()
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (E) 
- [0167. Two Sum II - Input array is sorted](Solutions/0167.Two-Sum-II-Input-array-is-sorted.py) (E)
- [0170. Two Sum III - Data structure design](Solutions/0170.Two-Sum-III-Data-structure-design.py) (E)
- [0653. Two Sum IV - Input is a BST](Solutions/0653.Two-Sum-IV-Input-is-a-BST.py) (E)
- [1099. Two Sum Less Than K](Solutions/1099.Two-Sum-Less-Than-K.py) (E) 
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) (求和用反向双指针，求差用同向双指针)
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (E) 
- [0015. 3Sum](Solutions/0015.3Sum.py) (!!M) 
- [0016. 3Sum Closest](Solutions/0016.3Sum-Closest.py) (M) 
- [0259. 3Sum Smaller](Solutions/0259.3Sum-Smaller.py) (M) 
- [0018. 4Sum](Solutions/0018.4Sum.py) (M) 
- [0454. 4Sum II](Solutions/0454.4Sum-II.py) (M) 


## [Two Pointers](/Two-pointers.py)
### 反向双指针
- [0977. Squares of a Sorted Array](Solutions/0977.Squares-of-a-Sorted-Array.py) (E) 
#### Partition
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode)
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E)
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) (三根指针partition成三个部分)
- [0561. Array Partition I](Solutions/0561.Array-Partition-I.py) (E) 



### 同向双指针
- [0283. Move Zeroes](Solutions/0283.Move-Zeroes.py) (E) 
- [0026. Remove Duplicates from Sorted Array](Solutions/0026.Remove-Duplicates-from-Sorted-Array.py) (E) 
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) 



## [Sorted Array]() 
- [0088. Merge Sorted Array](Solutions/0088.Merge-Sorted-Array.py) (E) 
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M) (quick select) 
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) (Binary search) 




## [SubArray](/SubArray.py)
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (！！E) (前缀和prefixSum)
- [0724. Find Pivot Index](Solutions/0724.Find-Pivot-Index.py) (E) (prefixSum)
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M) (prefixSum+hashmap)
- [0523. Continuous Subarray Sum](Solutions/0523.Continuous-Subarray-Sum.py) (M) (prefixSum+hashmap)
- [0974. Subarray Sums Divisible by K](Solutions/0974.Subarray-Sums-Divisible-by-K.py) (M) (prefixSum+hashmap)
- [0139. Subarray Sum Closest](Solutions/0139.Subarray-Sum-Closest.py) (Lintcode) (prefixSum+hashmap)



## [Linked List](/Linked-List)
- [0148. Sort List](Solutions/0148.Sort-List.py) (！！M)
- [0206. Reverse Linked List](Solutions/0206.Reverse-Linked-List.py) (！！E) (需要熟背理解)
- [0092. Reverse Linked List II](Solutions/0092.Reverse-Linked-List-II.py) (M)
- [0024. Swap Nodes in Pairs](Solutions/0024.Swap-Nodes-in-Pairs.py) (M)
- [0025. Reverse Nodes in k-Group](Solutions/0025.Reverse-Nodes-in-k-Group.py) (H)
- [0138. Copy List with Random Pointer](Solutions/0138.Copy-List-with-Random-Pointer.py) (M)
- [0141. Linked List Cycle](Solutions/0141.Linked-List-Cycle.py) (E)
- [0142. Linked List Cycle II](Solutions/0142.Linked-List-Cycle-II.py) (E)
- [0160. Intersection of Two Linked Lists](Solutions/0160.Intersection-of-Two-Linked-Lists.py) (E)
- [0021. Merge Two Sorted Lists](Solutions/0021.Merge-Two-Sorted-Lists.py) (E)
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (E)



## [Depth First Search](/Depth-First-Search.py)
### Combination
- [0078. Subsets](Solutions/0078.Subsets.py) (！！M)(DFS + Back tracking)
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (！！M)(如果之前的那个2没被放进去，那么就不要放后面那个2，这样来去重)
- [0039. Combination Sum](Solutions/0039.Combination-Sum.py) (！M) (start是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次)
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (！M) (与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解，用DFS+Backtracking超时)
- [0040. Combination Sum II](Solutions/0040.Combination-Sum-II.py) (！M) (避免重复输出的方法与Subsets II一样)
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (！M) (这个题更确切应该叫Permutatino Sum，TLE)
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (！M) (递归的定义很重要)

### Permutation
- [0046. Permutations](Solutions/0046.Permutations.py) (！！M)
- [0047. Permutations II](Solutions/0047.Permutations-II.py) (！！M) (去重方法与Subsets是类似的)
- [0051. N-Queens](Solutions/0051.N-Queens.py) (！H) (核心是nums=[0,1,2,3]的去重排列问题，去重需要做三个visited的判断)
- [0052. NQueens II](Solutions/0052.N-Queens-II.py) (H) 

### 图上的搜索（打印/输出所有满足条件的路径必用DFS）
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (！！H)（好神奇）



## [Breadth First Search](/Breadth-First-Search.py)
### BFS in Trees
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (！！M)
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (！M)
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (！E)
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (！M)
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (E)
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (H)

### BFS in Graphs
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (M)
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M)
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (！！LintCode M) (Topological Sorting)
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (！！M) (opological Sort)
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (！！M) (Naked Topological Sort)
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (M)

### BFS in Matrix !!(隐式图搜索问题)
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (M)
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) (需要层序遍历)
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (！！M) (需要层序遍历，利用对称解决LTE问题，也可以从两端同时开始BFS)
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (！！M) (层序遍历BFS，双端BFS看不太懂)
- [0317 Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (！！H) (选择1为起点做层序遍历的BFS)



## [Sort](/Sort.py) 
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (M) (quick sort vs. merge sort) 
- [0969. Pancake Sorting](Solutions/0969.Pancake-Sorting.py) (M) (two flips to move the max_num to the end of arr) 

- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (M) (quick select)
#### Partition
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (Lintcode)
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E)
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) (三根指针partition成三个部分)



## [Binary Tree, Divide and Conquer](/Binary-Tree-Divide-and-Conquer.py) 
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) (memorize the iterative version using stack)
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) (memorize the iterative version using stack)
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (E) (Divide and Conquer vs Traverse)
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (E)
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) (Divide and Conquer + Traverse)
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) (Divide and Conquer + Traverse + resultType)
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) (resultType, used for return multipule values)
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E)
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (M)
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E)
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E)
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M)
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (M) (这种改变成linked list的题真是一头雾水呀)
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (M)
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (M)
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M)
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (M)




## [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (E)
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) (Find end point using "double method", same as dynamic array)
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (E)
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (M)
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E)
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (M)
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (H)
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (LintCode) (找到minPos, 然后三步反转法)
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M)
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E)
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M)
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) (Construct a OOOXXX problem to find the first X)
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) (Think the 2D array as a long 1D array cuz the rows and cols are sorted)
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) (Start from bottom left, head to top right, each comparism rule out a colomn or a row)


## Rabin Karp Algorithm
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (E) (Rabin Karp Algorithm O(M+N), use Hashcode, ord(ch)-ord("a"))

