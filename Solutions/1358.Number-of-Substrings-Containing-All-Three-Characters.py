"""
1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""




"""
at least problem, 套用第一种模板：j往前跑
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ch_to_cnt = collections.defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):
            while j < len(s) and len(ch_to_cnt) < 3:
                ch_to_cnt[s[j]] += 1
                j += 1
            
            if len(ch_to_cnt) >= 3:
                res += len(s) - j + 1   # len(s) - j + 1 表示以 i 开头的valid_substring的个数
                
            ch_to_cnt[s[i]] -= 1
            if ch_to_cnt[s[i]] == 0:
                del ch_to_cnt[s[i]]
                
        return res
