# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(sample):
            if sample is None:
                return 
            sample.left, sample.right = sample.right, sample.left
            invert(sample.left)
            invert(sample.right)
        invert(root)
        return root