#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2259. 移除指定数字得到的最大结果.py
@Author ：HuntingGame
@Date ：2022-10-20 9:29 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        ans = []
        for i in range(len(number)):
            if number[i] == digit:
                ans.append(number[:i] + number[i+1:])
        ans.sort(key=lambda x:eval(x))
        return ans[-1]