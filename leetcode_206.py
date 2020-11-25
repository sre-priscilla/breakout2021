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
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            # 顾后
            next = curr.next
            # 瞻前
            curr.next = prev
            # 平移
            prev, curr = curr, next
        return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(head.to_list())

    tail = Solution().reverseList(head)
    print(tail.to_list())