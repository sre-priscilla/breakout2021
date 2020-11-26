from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.queue.rotate(-(len(self.queue) - 1))


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    stack = MyStack()
    assert stack.empty()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top() == 3
    assert stack.pop() == 3
