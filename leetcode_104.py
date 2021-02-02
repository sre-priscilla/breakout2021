# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque
        
        if root is None:
            return 0
        queue, level = deque([root]), 0
        while queue:     
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1
        return level
