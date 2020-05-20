437. Copy Books

Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

Example 1:

Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.


    
"""
binary search: O(nlog(sum(pages)-max(pages))), n is the number of books
"""
class Solution:
    def copyBooks(self, pages, k):
        """
        k is the number of person to copy the books
        """
        if not pages:
            return 0
            
        startTime, endTime = max(pages), sum(pages)
        while startTime + 1 < endTime:
            midTime = startTime + (endTime - startTime) // 2
            if self.leastPersonNeeded(pages, midTime) <= k:
                endTime = midTime
            else:
                startTime = midTime
                
        return startTime if self.leastPersonNeeded(pages, startTime) <= k else endTime
        
    def leastPersonNeeded(self, pages, timeLimit):
        """
        return the least person needed in order to finish all the pages in the timeLimit.  Algorithm: greedy. 每次发现要超时了就加一个人。
        sweep the books and keep track of the timeNeeded. 
        when we find we cannot finish all pages in timeLimit, we add a new person and set the timeNeeded for the new person to be zero
        """
        personNeeded = 1
        timeNeeded = 0      # initialize the timeNeeded for person 1 is zero
        for pages in pages:
            # whenever timeNeeded is over the timelimit, we need a new person to join and help, so that we can reduce the timeCost within timeLimit
            # 每次发现要超时了就加一个人
            if timeNeeded + page > timeLimit:    
                personNeeded += 1
                timeNeeded = 0        # timeNeeded resets to 0 for the new persion joined
            timeNeeded += page
            
        return personNeeded
    
    
    

"""需要找到一种分段方式，使得所有段的数字之和的最大值最小
f[k][i]=前k个(不包括k)抄写员最多需要多长时间抄完前i本书(不包括i)
f[k][j]=min(max(f[k-1][i], i~j所需时间)) for 0<i <j
初始条件：f[k][0]=0; f[0][0]=0; f[0][i] = inf for i > 0
O(N^2*K), O(N*K)"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        lens = len(pages)
        dp = [[float("inf")] * (lens + 1) for _ in range(k + 1)]
        
        for m in range(k + 1):
            dp[m][0] = 0
            for j in range(1, lens + 1):
                dp[0][j] = float("inf")
                
        for m in range(1, k + 1):
            for j in range(1, lens + 1):
                for i in range(j):
                    tempMax = max(dp[m - 1][i], sum(pages[i:j]))
                    dp[m][j] = min(dp[m][j], tempMax)
                    
        return dp[k][lens]
