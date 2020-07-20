1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.



"""
what we need to append into res is the nodes that are roots and not in to_delete list.
we need to pass is_root bool into the helper function to determine whether of not 
we should append it into res.  If it is root and not in to_delete_set, then we should append into res.
"""
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def helper(root, is_root):
            if not root:
                return None

            should_delete = root.val in to_delete_set
            
            if is_root and not should_delete:
                res.append(root)
            
            root.left = helper(root.left, should_delete)  # if the root should be deleted, then root.left becomes a new root of a forest
            root.right = helper(root.right, should_delete)
            
            return root if not should_delete else None
            
            
        to_delete_set = set(to_delete)
        res = []
        helper(root, True)
        return res
