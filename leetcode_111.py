# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque
        
        if root is None:
            return 0
        queue, level = deque([root]), 0
        while queue:     
            n, level = len(queue), level + 1
            for i in range(n):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return level
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return level