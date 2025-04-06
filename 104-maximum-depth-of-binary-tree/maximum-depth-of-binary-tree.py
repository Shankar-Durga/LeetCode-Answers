# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def depth(sample,count):
            if sample is None:
                return count
            return max(depth(sample.left,count+1),depth(sample.right,count+1))
            

        return max(depth(root.left,1),depth(root.right,1))
        
