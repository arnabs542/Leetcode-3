#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.26%)
# Likes:    3018
# Dislikes: 84
# Total Accepted:    179.2K
# Total Submissions: 413.4K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#


"""
我们先构造一个数组pre_sum, 然后接下来就和two sum problem是一样的了，
two sum是寻找两数之和：nums[i]+nums[j] = k, 这里是寻找两数之差：pre_sum[j] - pre_sum[i] = k. 
方法都是用hashmap记录访问过的nums[i], O(N), O(N)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum_dict = defaultdict(int)  # pre_sum --> cnt of the occurance of the pre_sum
        pre_sum_dict[0] = 1  # 特别注意pre_sum_dict需要初始化!!!!

        # Our problem is: find how many pairs of <i,j> satisfies prefix_sum[j] - prefix_sum[i] == k?
        # 接下来是 two sum 问题
        pre_sum = 0
        cnt = 0
        for i, num in enumerate(nums):
            pre_sum += num  # 这里的pre_sum相当于prefix_sum[j+1], 一般都不会单独开一个数组出来存prefix_sum
            if pre_sum - k in pre_sum_dict:  # 等价于if prefix_sum[j] - prefix_sum[i] == k
                cnt += pre_sum_dict[pre_sum - k]

            pre_sum_dict[pre_sum] += 1  # 将 pre_sum 存入pre_sum_dict中

        return cnt


"""
Solution 2: prefixSum (TLE)
find all the subArrSum by using subArrSum(i~j) = prefixSum[j+1] - prefixSum[i]
O(N^2), O(N)"""
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构造prefixSum[i]: the sum of all items before i
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        cnt = 0
        for j in range(len(nums)):
            for i in range(j + 1):
                # subArrSum(i~j包含i和j) = prefixSum[j+1] - prefixSum[i] 
                # i==j时，subArr只有一个元素，所以i是可以等于j的，这就是为什么i in range(j + 1)
                if prefixSum[j+1] - prefixSum[i] == k:
                    cnt += 1

        return cnt



"""
Solution 1: Brutal Force (TLE)
find all the subArrSum by using sum(nums[i:j])
O(N^3), O(1)"""
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for j in range(len(nums) + 1):
            for i in range(j):
                subArrSum = sum(nums[i:j])
                if subArrSum == k:
                    cnt += 1

        return cnt
