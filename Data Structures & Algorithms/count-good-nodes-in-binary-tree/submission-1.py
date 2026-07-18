# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_nodes_count = 0
        q = deque([(root, float("-inf"))])
        while q:
            node, max_so_far = q.popleft()
            
            if node.val >= max_so_far:
                good_nodes_count += 1
            current_max = max(max_so_far, node.val)

            if node.left:
                q.append((node.left, current_max))
            if node.right:
                q.append((node.right, current_max))
        
        return good_nodes_count 