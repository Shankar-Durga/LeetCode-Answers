# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checker(i,j):
            if i is None and j is None:
                return True
            if i is None or j is None:
                return False
            return i.val == j.val and checker(i.left, j.left) and checker(i.right,j.right)
        
        return checker(p,q) 