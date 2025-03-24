# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validator(low, high, node):
            if node is None:
                return True
            if (low is not None and node.val <= low) or (high is not None and node.val>=high):
                    return False
            return validator(low, node.val, node.left) and validator(node.val, high, node.right)


        return validator(None,None,root)