# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     inorder: List[int] = self.LMR(root)
    #     return self.LMR(root) == list(sorted(set(inorder)))

    # def LMR(self, root: TreeNode) -> List[int]:
    #     if root is None:
    #         return []
    #     return [*self.LMR(root.left), root.val, *self.LMR(root.right)]

    # def isValidBST(self, root: TreeNode) -> bool:
    #     self.prev: TreeNode = None
    #     return self.helper(root)

    # def helper(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return True
    #     if not self.helper(root.left):
    #         return False
    #     if self.prev and self.prev.val >= root.val:
    #         return False
    #     self.prev = root
    #     return self.helper(root.right)

    # def isValidBST(self, root: TreeNode) -> bool:
    #     return self.validate(root, None, None)

    # def validate(self, root: TreeNode, _min: Optional[int], _max: Optional[int]) -> bool:
    #     if root is None:
    #         return True
    #     if not (_min is None) and root.val <= _min:
    #         return False
    #     if not (_max is None) and root.val >= _max:
    #         return False
    #     return self.validate(root.left, _min, root.val) and self.validate(root.right, root.val, _max)

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        prev, stack = None, []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev, root = root, root.right
        return True

