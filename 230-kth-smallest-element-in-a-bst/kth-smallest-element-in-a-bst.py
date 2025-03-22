# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def checker(root):
            if root is None:
                return 
            checker(root.left)
            ans.append(root.val)
            checker(root.right)
        checker(root)
        return ans[k-1]
