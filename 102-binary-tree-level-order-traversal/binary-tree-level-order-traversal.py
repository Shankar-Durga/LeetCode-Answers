# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# cur_queue = [], next_queue=[], level = [], result = [[3],[9,20],[15,7]]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return[]
        
        cur_queue = [root]
        next_queue = []
        level = []
        result = []
        while cur_queue:
            for i in cur_queue:
                level.append(i.val)
                if i.left:
                    next_queue.append(i.left)
                if i.right:
                    next_queue.append(i.right)
            result.append(level)
            cur_queue = next_queue
            next_queue,level = [],[]
        return result 
            