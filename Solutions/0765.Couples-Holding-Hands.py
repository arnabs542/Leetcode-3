765. Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.


"""
solution 1 暴力法：从左至右依次配对好 - O(N^2)
"""
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swap = 0
        for i in range(0, len(row), 2):
            couple_num = row[i] ^ 1     # 偶数xor 1相当于+1, 奇数xor 1相当于-1
            for j in range(i+2, len(row)):
                if row[j] == couple_num:
                    row[i+1], row[j] = row[j], row[i+1]
                    swap += 1
                    break
        return swap
        
        
        
        
"""
solution 2: union find - O(N). 
step 1: initialize by connecting 0-1, 2-3, 4-5....
step 2: we traverse the row, and union row[i] and row[i+1],
if needs to be unioned, then that means needs one swap to make it row[i] and row[i+1] a couple.
"""
class UnionFind:
    
    def __init__(self, n):
        self.father = collections.defaultdict()
        self.cnt = 0
        for i in range(0, n, 2):    # step 1: initialize
            self.add(i)
            self.add(i+1)
            self.union(i, i+1)
    
    def add(self, x):
        self.father[x] = x
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            self.father[rootx] = rooty
            self.cnt += 1   # if needs to be unioned, then that means needs one swap to make it row[i] and row[i+1] a couple.         


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        uf = UnionFind(len(row))
        for i in range(0, len(row), 2):
            x, y = row[i], row[i+1]
            uf.union(x, y)
        return uf.cnt - len(row)//2       # 减去len(row)//2是因为uf object在initialize的时候就已经有len(row)//2个components了
