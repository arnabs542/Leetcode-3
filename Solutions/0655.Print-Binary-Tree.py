655. Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def helper(root, depth, pos):
            res[-(depth+1)][pos] = str(root.val)
            if root.left:
                helper(root.left, depth-1, pos-2**(depth-1))
            if root.right:
                helper(root.right, depth-1, pos+2**(depth-1))

        depth = self._find_depth(root)
        m, n = depth, 2 ** depth - 1
        res = [["" for _ in range(n)] for _ in range(m)]
        
        helper(root, depth-1, 2**(depth-1)-1)
        return res
        
        
    def _find_depth(self, root):
        if not root:
            return 0
        return 1 + max(self._find_depth(root.left), self._find_depth(root.right))
