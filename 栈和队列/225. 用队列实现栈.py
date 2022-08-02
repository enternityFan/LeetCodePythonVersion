# @Time : 2022-08-02 9:37
# @Author : Phalange
# @File : 225. 用队列实现栈.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class MyStack:
    """
    对于[1,2,3]:
    1. q1:[],q2:[1]   <---> q1:[1],q2:[]
    2. q1:[],q2[2,1]  <---> q1:[2,1],q2:[]
    3. q1:[],q3[3,2,1] <---> q1:[3,2,1],q2:[]


    """

    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue2.append(x) #首先给压到2中
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1,self.queue2 = self.queue2,self.queue1


    def pop(self) -> int:
        return self.queue1.popleft()


    def top(self) -> int:
        return self.queue1[0]


    def empty(self) -> bool:
        return not self.queue1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()