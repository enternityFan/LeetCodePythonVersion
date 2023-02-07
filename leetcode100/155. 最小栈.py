#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：155. 最小栈.py
@Author ：HuntingGame
@Date ：2023-02-07 19:18 
C'est la vie!!! enjoy ur day :D
'''
class MinStack:

    def __init__(self):
        """
        这个题两个栈，一个数据栈，一个最小栈。
        """
        self.data = []
        self.mindata = []


    def push(self, val: int) -> None:
        self.data.append(val)
        if self.mindata == []:
            self.mindata.append(val)
        else:
            self.mindata.append(min(self.mindata[-1],val))


    def pop(self) -> None:
        self.mindata.pop()
        self.data.pop()


    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.mindata[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()