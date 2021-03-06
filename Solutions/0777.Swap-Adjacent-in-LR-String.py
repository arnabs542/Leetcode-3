"""
777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". 
Given the starting string start and the ending string end, 
return True if and only if there exists a sequence of moves to transform one string to the other.

Example 1:

Input: start = "X", end = "L"
Output: false
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "LLR", end = "RRL"
Output: false
Example 3:

Input: start = "XLLR", end = "LXLX"
Output: false
 
Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""


"""
观察之后可以发现每次replace "XL" to "LX"都是相当于把"L"向左移动。
所以"L"一直向左移动，并且不会跨越其他"L" or "R". 而"R"一直向右移动，并且不会跨越其他"R" or "L".
所以：
1. start和end中"L"和"R"的个数和顺序必须相同;
2. "L"在start中对应的index必须大于"L"在end中对应的index, 因为start中的"L"能且只能向左移动;
3. "R"在start中对应的index必须小于"R"在end中对应的index, 因为start中的"E"能且只能向右移动
"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if Counter(start) != Counter(end):
            return False
        
        start_idx = [(i, start[i]) for i in range(len(start)) if start[i] == "L" or start[i] == "R"]
        end_idx = [(i, end[i]) for i in range(len(end)) if end[i] == "L" or end[i] == "R"]
        
        for i in range(len(start_idx)):
            s_pos, s_ch = start_idx[i]
            e_pos, e_ch = end_idx[i]
            
            if s_ch != e_ch:    # "R" or "L" 无法跨越其他 "R" or "L"
                return False
            
            if s_ch == "L" and s_pos < e_pos:       # "L"只能向左移动
                return False
            elif s_ch == "R" and s_pos > e_pos:     # "R"只能向右移动
                return False
            
        return True
