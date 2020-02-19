Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1


"""OOOXXX问题，找到第一个出现的X，X是the first position of 递减的序列"""
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lens = len(A)
        start, end = 0, lens - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= A[mid+1]:
                end = mid
            else:
                start = mid

    return start if A[start] > A[end] else end
