# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def checker(self, tree, subRoot):
    #     if tree is None and subRoot is None:
    #         return True
    #     if tree is None or subRoot is None:
    #         return False

    #     return tree.val == subRoot.val and self.checker(tree.left, subRoot.left) and self.checker(tree.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def checker( tree, subRoot_test):
            if tree is None and subRoot_test is None:
                return True
            if tree is None or subRoot_test is None:
                return False

            return tree.val == subRoot_test.val and checker(tree.left, subRoot_test.left) and checker(tree.right, subRoot_test.right)
        return checker(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

            
