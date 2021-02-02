from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if root is None:
            return []
        queue, ret = deque([root]), []
        while queue:
            n, tmp = len(queue), []
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ret.append(tmp)
        return ret