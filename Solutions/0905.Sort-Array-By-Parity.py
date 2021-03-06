#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (73.29%)
# Likes:    687
# Dislikes: 67
# Total Accepted:    152.8K
# Total Submissions: 208.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#


"""
anchor keeps all the even number on it's left side;
curr keeps going until hit an even number, then switch the even number to anchor
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        anchor = 0
        curr = 0
        for curr in range(len(nums)):
            if nums[curr] % 2 == 0:
                nums[anchor], nums[curr] = nums[curr], nums[anchor]
                anchor += 1
        return nums


"""
用双指针的方法做partition，与lintcode 31的方法一模一样
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] % 2 == 0:
                left += 1
            while left <= right and A[right] % 2 == 1:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
                
        return A
