# @Time : 2022-08-02 10:32
# @Author : Phalange
# @File : 面试题 03.04. 化栈为队.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack1.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return len(self.stack1) == 0


arr = MyQueue()
print(arr.push(1))
print(arr.push(2))
print(arr.peek())
print(arr.pop())