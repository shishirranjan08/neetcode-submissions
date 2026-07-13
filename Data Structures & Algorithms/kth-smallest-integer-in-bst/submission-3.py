# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = None

        def walk(node):
            if node is None:
                return
            walk(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return
            walk(node.right)
        
        walk(root)
        return self.answer
            


        