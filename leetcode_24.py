# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def to_list(self):
        elms, curr = [], self
        while curr:
            elms.append(curr.val)
            curr = curr.next
        return elms

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        _head = prev = ListNode(-1, head)
        curr = head
        while curr and curr.next:
            next = curr.next
            curr.next, next.next = next.next, curr
            prev.next = next
            prev, curr = curr, curr.next
        return _head.next


if __name__ == '__main__':
    head = ListNode(1)
    print(Solution().swapPairs(head).to_list())
    
    head = ListNode(1)
    head.next = ListNode(2)
    print(Solution().swapPairs(head).to_list())
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(Solution().swapPairs(head).to_list())

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(Solution().swapPairs(head).to_list())
