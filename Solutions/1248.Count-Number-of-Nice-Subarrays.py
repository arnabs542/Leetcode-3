"""
1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""



"""
This problem will be a very typical sliding window,
if it asks the number of subarrays with at most K distinct elements.
Just need one more step to reach the folloing equation:
exactly(K) = atMost(K) - atMost(K-1); 
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self._at_most(nums, k) - self._at_most(nums, k - 1)
    
    # 套用第二种模板：find max subarray size for at most problem.
    def _at_most(self, nums, k):
        odd_cnt = 0
        res = 0
        i = 0
        for j in range(len(nums)):
            odd_cnt += nums[j] % 2          # 总是先更新后面的指针j
            
            while i <= j and odd_cnt > k:
                odd_cnt -= nums[i] % 2      
                i += 1
            
            if odd_cnt <= k:                
                res += j - i + 1
                
        return res
