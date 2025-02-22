# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validator(node, min_value, max_value):
            if node is None:
                return True
            if (min_value is not None and node.val<=min_value) or ( max_value is not None and node.val>=max_value ):
                return False
            return (validator(node.left, min_value,node.val) and validator(node.right,node.val,max_value) )
        return validator(root, None,None) 