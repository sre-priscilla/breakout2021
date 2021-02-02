class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if root is None or root is p or root is q:
    #         return root
    #     l = self.lowestCommonAncestor(root.left, p, q)
    #     r = self.lowestCommonAncestor(root.right, p, q)  
    #     if l is None:
    #         return r
    #     if r is None:
    #         return l
    #     return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from collections import deque

        if root is None:
            return None

        queue = deque([root])
        parent_map = {root: None}
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    parent_map[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parent_map[node.right] = node
        _p, path_p = p, []
        while _p and _p in parent_map:
            path_p.append(_p)
            _p = parent_map[_p]
        _q, path_q = q, []
        while _q and _q in parent_map:
            path_q.append(_q)
            _q = parent_map[_q]
        n = min(len(path_p), len(path_q))
        post = None
        while path_p and path_q:
            a, b = path_p.pop(), path_q.pop()
            if a is b:
                post = a
        return post


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.right
    print(Solution().lowestCommonAncestor(root, p, q).val)

    q = root.left.right.right
    print(Solution().lowestCommonAncestor(root, p, q).val)

        



                