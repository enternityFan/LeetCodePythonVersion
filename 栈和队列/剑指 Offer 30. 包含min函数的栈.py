#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 30. 包含min函数的栈.py
@Author ：HuntingGame
@Date ：2023-03-07 13:22 
C'est la vie!!! enjoy ur day :D
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minstack.append(x)
        elif x < self.minstack[-1]:
            self.stack.append(x)
            self.minstack.append(x)
        else:
            self.stack.append(x)
            self.minstack.append(self.minstack[-1])


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:

        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()