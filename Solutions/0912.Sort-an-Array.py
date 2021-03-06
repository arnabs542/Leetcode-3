# solution 2: quick sort
"""
另一个采用分而治之策略的排序算法是快速排序，其优势是不需要额外的存储空间，这一点比归并排序强。
快速排序的思路是依据一个“中值”数据项来把数据表分为两半：小于中值的一半和大于中值的一半，然后每部分分别进行快速排序
输入list, i, j; 输出：list中以list[i]为pivot分为左右两边，左边小于pivot，右边大于；输出分边之后pivot所在的位置。
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, start, end):
        if start >= end:    # the outlet of the recursion is start >= end
            return
        
        # 先整体有序
        # 注意这里选取pivot原因不能保证recursion tree深度稳定在log(N)，最坏的情况是深度为N.
        pivot = nums[(start + end) // 2]     # key point 1: pivot is the value, not the index 
        left, right = start, end
        while left <= right:        # key point 2: it should be left <= right not left < right
            while left <= right and nums[left] < pivot:   # key point 3: it should be nums[left] < pivot
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # 再局部有序, 注意出while循环之后right在左边，所以这里是right
        self.quickSort(nums, start, right)  # no return for the quickSort function!
        self.quickSort(nums, left, end)
        
        
# solution 1: merge sort (top down recurssion)
# there are logN merge operations and each merging takes O(N) operations. That is why the time complexity is O(NlogN)
def sortArray(self, nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    # ste p1: divide - 由于每次都是稳定取中间进行divide
    # 所以recursion tree的深度可以稳定在log(N)
    mid = len(nums) // 2 
    leftArr = self.sortArray(nums[:mid])
    rightArr = self.sortArray(nums[mid:])

    # step 2: conquer
    i, j, k = 0, 0, 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            nums[k] = leftArr[i]
            i += 1
            k += 1
        else:
            nums[k] = rightArr[j]
            j += 1
            k += 1
    while i < len(leftArr):
        nums[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        nums[k] = rightArr[j]
        j += 1
        k += 1

    return nums
