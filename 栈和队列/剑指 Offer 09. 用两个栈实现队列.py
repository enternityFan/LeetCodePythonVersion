#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 09. 用两个栈实现队列.py
@Author ：HuntingGame
@Date ：2023-03-06 18:20 
C'est la vie!!! enjoy ur day :D
'''
class CQueue:

    def __init__(self):
        self.A,self.B = [],[]


    def appendTail(self, value: int) -> None:
        self.A.append(value)


    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1#,AB都为[]说明没有元素
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()