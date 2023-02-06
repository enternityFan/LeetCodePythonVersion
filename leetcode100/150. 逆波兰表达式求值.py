#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：150. 逆波兰表达式求值.py
@Author ：HuntingGame
@Date ：2023-02-06 18:41 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def __init__(self):
        self.stack = []
    def evalRPN(self, tokens: List[str]) -> int:
        """
        这个题就是用栈区做的。
        :param tokens:
        :return:
        """
        for each in tokens:
            if each == "+" or each == "-" or each == "*" or each == "/":
                self.compute(each)
            else:
                self.stack.append(int(each))
        return int(self.stack[-1])

    def compute(self,op):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        ans = 0
        if op == "+":
            ans = num1+num2
        elif op == "-":
            ans = num1 - num2
        elif op == "*":
            ans = num1 * num2
        elif op == "/":
            ans = num1 / num2
        self.stack.append(ans)


print(Solution().evalRPN(["2","1","+","3","*"]))

