# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def elements(root):
            if not root: return ["null"] 

            left = elements(root.left)
            right = elements(root.right)

            return [root.val] + left + right
        
        return elements(p) == elements(q)
        