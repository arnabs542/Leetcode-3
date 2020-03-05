75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


"""typical partition problem"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        
        # step 1: 先把0放到最前面
        i, j = 0, lens - 1
        temp = nums[i]
        while i < j:
            while i < j and nums[j] > 0:
                j -= 1
            nums[i] = nums[j]
            
            while i < j and nums[i] == 0:
                i += 1
            nums[j] = nums[i]
            
        nums[i] = temp

        # step 2: 再把2放到最后
        m = i + 1 if nums[i] == 0 else i
        n = lens - 1
        if m >= n:
            return nums
        
        temp = nums[m]
        while m < n:
            while m < n and nums[n] == 2:
                n -= 1
            nums[m] = nums[n]
            
            while m < n and nums[m] < 2:
                m += 1
            nums[n] = nums[m]
            
        nums[m] = temp
    
    
    
"""同向双指针: move '2's to the right first, then move '1's to the right
这种分区的题目都可以用同向双指针"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lens = len(nums)
        anchor, curr = 0, 0
        while curr < lens:
            if nums[curr] == 2:
                curr += 1
            else:
                nums[anchor], nums[curr] = nums[curr], nums[anchor]
                anchor += 1
                curr += 1
                
        # after the while loop, anchor is at the first '2' position
        
        anchor1, curr = 0, 0
        while curr < anchor:
            if nums[curr] == 1:
                curr += 1
            else:
                nums[anchor1], nums[curr] = nums[curr], nums[anchor1]
                anchor1 += 1
                curr += 1    
    
    
    
"""使用一次扫描的办法。
设立三根指针，left, index, right。定义如下规则：
left 的左侧都是 0（不含 left）
right 的右侧都是 2（不含 right）
index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管。"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        lens = len(nums)
        left, index, right = 0, 0, lens - 1
        while index <= right:       # be careful, index < right is not correct  （不太懂）
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            elif nums[index] == 1:  
                index += 1
        
        return nums
