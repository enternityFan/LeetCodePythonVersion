#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 46. 把数字翻译成字符串.py
@Author ：HuntingGame
@Date ：2023-03-15 20:45 
C'est la vie!!! enjoy ur day :D
'''
import math


class Solution:
    def translateNum(self, num: int) -> int:
        if num <=9:return 1
        if num <=25:return 2

        tmp = self.translateNum(num // 100) if (num % 100 <= 25 and num % 100 >=10) else 0
        return self.translateNum(num // 10) + tmp

print(Solution().translateNum(10))