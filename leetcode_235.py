from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if p.val < root.val > q.val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     if p.val > root.val < q.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     return root

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     while root:
    #         if p.val < root.val > q.val:
    #             root = root.left
    #         elif p.val > root.val < q.val:
    #             root = root.right
    #         else:
    #             return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.find_path(root, p)
        path_q = self.find_path(root, q)
        if len(path_p) == 0 or len(path_q) == 0:
            return None
        n = min(len(path_p), len(path_q))
        prev = None
        for i in range(n):
            if path_p[i] is path_q[i]:
                prev = path_p[i]
            else:
                break
        return prev


    def find_path(self, root: TreeNode, target: TreeNode) -> List[TreeNode]:
        if root is None:
            return []
        curr, path = root, []
        while curr:
            path.append(curr)
            if curr.val > target.val:
                curr = curr.left
            elif curr.val < target.val:
                curr = curr.right
            else:
                break
        return path
    

if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = root.left
    q = root.right
    print(Solution().lowestCommonAncestor(root, p, q).val)

    q = root.left.right
    print(Solution().lowestCommonAncestor(root, p, q).val)

