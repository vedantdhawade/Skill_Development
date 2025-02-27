from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxdepth(node):
            if node is None:  # Base case: empty node has depth 0
                return 0
            return 1 + max(maxdepth(node.left), maxdepth(node.right))

        return maxdepth(root)  # Call the helper function
