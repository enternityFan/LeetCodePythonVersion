#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 19:37
# @Author  : HuntingGame
# @FileName: 1433. 检查一个字符串是否可以打破另一个字符串.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        flag = True

        for i in range(len(s1)):
            if s1[i] > s2[i]:
                flag= False
                break
        if flag:
            return True
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                return False
        return True





