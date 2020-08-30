307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.


class SegmentTree:
    
    def __init__(self, start, end, range_sum):
        self.start = start
        self.end = end
        self.range_sum = range_sum
        self.left = None
        self.right = None
        
    def build(self, start, end, arr):
        if start > end:
            return None
        
        root = SegmentTree(start, end, arr[start])
        if start == end:
            return root
        
        mid = start + (end - start) // 2
        root.left = self.build(start, mid, arr)
        root.right = self.build(mid + 1, end, arr)
        root.range_sum = root.left.range_sum + root.right.range_sum      
        
        return root

    def query(self, root, start, end):
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.range_sum
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)
    
    def update(self, root, idx, val):
        if not root:
            return
        if root.start == root.end:
            root.range_sum = val
            return
        
        if root.left.end >= idx:
            self.update(root.left, idx, val)
        else:
            self.update(root.right, idx, val)
        
        root.range_sum = root.left.range_sum + root.right.range_sum


class NumArray:

    def __init__(self, arr: List[int]):
        self.sgtree = SegmentTree(0, len(arr) - 1, 0)
        self.root = self.sgtree.build(0, len(arr) - 1, arr)

    def update(self, i: int, val: int) -> None:
        self.sgtree.update(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.sgtree.query(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
