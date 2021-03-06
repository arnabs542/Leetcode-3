"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

   
"""
solution 1: O(N^2)
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        root = TreeNode()
        root.val = postorder.pop()
        
        idx = 0
        for i, num in enumerate(inorder):
            if num == root.val:
                idx = i
                break
        
        root.right = self.buildTree(inorder[idx+1:], postorder) # 注意要先更新right, 这是因为我们需要对postorder做pop
        root.left = self.buildTree(inorder[:idx], postorder)    # 只有先把后面的pop出来才能去pop前面的，而postorder后面的对应的是right部分
        
        return root
        
        
        
"""
solution 1 takes O(N^2) because each time we find idx in inorder, it takes O(N).
We can use a hash table to store the num-to-idx pair in advance.
This leads to solution 2, which is O(N) instead of O(N^2).
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(start, end):
            if start >= end:
                return None
            
            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1
            idx = num_idx[root.val]
            
            root.right = build(idx + 1, end)        # 注意right要放到left前面更新
            root.left = build(start, idx)        
        
            return root
        
        
        num_idx = defaultdict(int)
        for idx, num in enumerate(inorder): 
            num_idx[num] = idx
            
        self.post_idx = len(postorder) - 1
        return build(0, len(inorder))
