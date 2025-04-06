# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checker(self, tree, subRoot):
        if tree is None and subRoot is None:
            return True
        if tree is None or subRoot is None:
            return False

        return tree.val == subRoot.val and self.checker(tree.left, subRoot.left) and self.checker(tree.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.checker(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

            
