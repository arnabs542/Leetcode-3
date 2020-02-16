Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true


"""f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成
f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return False
        
        lens1, lens2, lens3 = len(s1), len(s2), len(s3)
        if lens1 + lens2 != lens3:
            return False
        
        dp = [[False] * (lens2 + 1) for _ in range(lens1 + 1)]
        
        dp[0][0] = True
        
        for i in range(1, lens1 + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                dp[i][0] = False
                
        for j in range(1, lens2 + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                dp[0][j] = False
                
        for i in range(1, lens1 + 1):
            for j in range(1, lens2 + 1):
                if s3[i + j -1] == s1[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
                    
        return dp[-1][-1]
