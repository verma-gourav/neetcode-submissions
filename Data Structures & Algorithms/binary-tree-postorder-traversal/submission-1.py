# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        stack = [(root, False)]  # (curr, children_processed)

        while stack:
            curr, children_processed = stack.pop()

            if children_processed:
                res.append(curr.val)
            else:
                stack.append((curr, True))

                if curr.right:
                    stack.append((curr.right, False))
                if curr.left:
                    stack.append((curr.left, False))

        return res