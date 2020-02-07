动态规划一般用来求最优解或者求有多少解，而打印出所有的解是动态规划做不了的，必须用递归或DFS来做。

动态规划题目的特点：
1.  计数
       - 有多少种方式走到右下角 
       - 有多少种方法选出k个数使得和是Sum
eg: 62. Unique Paths
       
2.  求最大最小值！  （扣题目字眼，如find maximum sum, minimum cost, maximum length等）
       - 从左上角走到右下角路径的最大数字和
       - 最长上升子序列长度
eg: 322. Coin Change; 120. Triangle; 152. Maximum Product Subarray
       
3.  求存在性
       - 取石子游戏，先手是否必胜
       - 能不能选出k个数使得和是Sum
eg: 55. Jump Game
       

动态规划四个组成部分：
1. 确定状态
• 研究最优策略的最后一步
• 化为子问题
2. 转移方程
• 根据子问题定义直接得到
3. 初始条件和边界情况
• 细心，考虑周全
4. 计算顺序
• 利用之前的计算结果
       
    
第一讲：坐标型动态规划: 62. Unique Paths； 63. Unique Path II； 64. Minimum Path Sum
题目特点：
给定一个序列或网格，需要找到序列中的子序列/网格中的某条路径的
- 最大值/最小值
- 计数
- 存在性
这类题目的状态通常定义为：                           
f(i)表示以(i)结尾的子序列的最大值/最小值或者计数或者存在性；初始条件为f(0) 
f(i,j)表示以(i,j)结尾的路径最大值/最小值或者计数或者存在性；初始条件为f(0,0)或者f(i,0)或者f(0,j)                                                       
                              
第二讲：序列型动态规划 
256. Paint House
f(i)表示以(i)结尾的子序列的某种性质如最大值/最小值或者计数或者存在性；初始条件为f(0)
分支：最长序列型 300. Longest Increasing Subsequence


第三讲：划分型动态规划 
91. Decode Ways
状态往往定义为前i个的某种特性，不包括i
eg 132: f[j]=the minimum number of total palindrom a palindrome partitining before the jth character (meaning the last palindrome should end with the j-1th character)
f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome
                              
                              
                              
                              
                              
                              

第四讲：位操作型动态规划 
338. Counting Bits
知识点：和位操作相关的动态规划一般用值作为状态



       
动态规划组成部分（以322.Coin Change为例）
1.1. 确定状态
• 状态在动态规划中的作用属于定海神针。简单的说，解动态规划的时候需要开一个数组，数组的每个元素f[i]或者f[i][j]代表什么
确定状态需要两个意识：
– 最后一步
– 子问题

1.2. 最后一步
• 虽然我们不知道最优策略是什么，但是最优策略肯定是K枚硬币a1, a2,…, aK 面值加起来是27
• 所以一定有一枚最后的硬币: aK
• 除掉这枚硬币，前面硬币的面值加起来是27 - aK
关键点1: 我们不关心前面的K-1枚硬币是怎么拼出27- aK的（可能有1种拼法，可能有100种拼法），而且我们现在甚至还不知道aK和K，但是我们确定前面的硬币拼出了27 - aK 
关键点2: 因为是最优策略，所以拼出27 - aK 的硬币数一定要最少，否则这就不是最优策略了

1.3. 子问题
• 所以我们就要求：最少用多少枚硬币可以拼出27 - aK
• 原问题是最少用多少枚硬币拼出27
• 我们将原问题转化成了一个子问题，而且规模更小：27 - aK
• 为了简化定义，我们设状态f(X)=最少用多少枚硬币拼出X

• 等等，我们还不知道最后那枚硬币aK是多少
• 最后那枚硬币aK只可能是2，5或者7
• 如果aK是2，f(27)应该是f(27-2) + 1 (加上最后这一枚硬币2）
• 如果aK是5，f(27)应该是f(27-5) + 1 (加上最后这一枚硬币5）
• 如果aK是7，f(27)应该是f(27-7) + 1 (加上最后这一枚硬币7）
• 除此以外，没有其他的可能了
• 需要求最少的硬币数，所以：f(27) = min{f(27-2)+1, f(27-5)+1, f(27-7)+1}

递归解法的问题
• 做了很多重复计算，效率低下，指数级别
• 如何避免？
• 将计算结果保存下来，并改变计算顺序

2. 转移方程
• 设状态f[X]=最少用多少枚硬币拼出X
• 对于任意X, f[X] = min{f[X-2]+1, f[X-5]+1, f[X-7]+1}

3. 初始条件和边界情况（初始条件是转移方程算不出来的；边界条件是不要数组越界）
• f[X] = min{f[X-2]+1, f[X-5]+1, f[X-7]+1}
• 两个问题：X-2, X-5 或者X-7小于0怎么办？什么时候停下来？
• 如果不能拼出Y，就定义f[Y]=正无穷
– 例如f[-1]=f[-2]=…=正无穷
• 所以f[1] =min{f[-1]+1, f[-4]+1,f[-6]+1}=正无穷, 表示拼不出来1
• 初始条件：f[0] = 0

4. 计算顺序（确定方法：想要算f[x]的时候右边用过的状态都已经算过了）
• 拼出 X 所需要的最少硬币数： f[X] = min{f[X-2]+1, f[X-5]+1, f[X-7]+1}
• 初始条件：f[0] = 0
• 然后计算f[1], f[2], …, f[27]
• 当我们计算到f[X]时，f[X-2], f[X-5], f[X-7]都已经得到结果了

算法复杂度：
• 每一步尝试三种硬币，一共27步
• 与递归算法相比，没有任何重复计算
• 算法时间复杂度（即需要进行的步数）： 27 * 3





