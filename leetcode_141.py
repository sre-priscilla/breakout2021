# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        p, nums = self, []
        while p:
            nums.append(p.val)
            p = p.next
        return nums

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        有环的链表没有终点
        p: t = s/v
        q: t = 2s/2v
        meet：2s/2v == s/v
        '''
        p, q = head, head
        while p and q:
            # p走一步
            if not p.next:
                return False
            else:
                p = p.next
            # q走两步
            if not q.next:
                return False
            else:
                q = q.next
            if not q.next:
                return False
            else:
                q = q.next
            # pq相遇证明链表有环
            if p is q:
                return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    print(Solution().hasCycle(head))