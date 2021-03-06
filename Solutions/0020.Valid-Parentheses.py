"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


"""
不能用简单的用三个counter, 会过不了这种情况: "([)]".
这题的题眼是a sub-expression of a valid expression should also be a valid expression. 所以用stack.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        mapping = {"(": ")", "[": "]", "{": "}"}
        
        st = []
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if len(st) == 0 or mapping[st[-1]] != ch:
                    return False
                st.pop()
        return len(st) == 0
