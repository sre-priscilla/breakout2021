class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        stack = [x]
        tmp = []
        for _ in range(len(self.stack)):
            tmp.append(self.stack.pop())
        for _ in range(len(tmp)):
            stack.append(tmp.pop())
        self.stack = stack




    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0



if __name__ == '__main__':
    queue = MyQueue()
    assert queue.empty()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.peek() == 1