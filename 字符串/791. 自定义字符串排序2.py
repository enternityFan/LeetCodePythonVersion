#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 17:08
# @Author  : HuntingGame
# @FileName: 791. 自定义字符串排序2.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnts = collections.Counter(s)
        ans = ""
        for c in order:
            if c in cnts and cnts[c] !=0:
                ans +=c * cnts[c]
                cnts[c] =0

        for key,val in cnts.items():
            if val !=0:
                ans +=key * val

        return ans

