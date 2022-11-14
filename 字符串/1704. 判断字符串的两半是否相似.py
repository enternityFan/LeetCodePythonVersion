#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 18:32
# @Author  : HuntingGame
# @FileName: 1704. 判断字符串的两半是否相似.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections


class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        a = s[:len(s)//2]
        b = s[len(s)//2:]
        cnt1 = collections.Counter(a)
        cnt2 = collections.Counter(b)
        c1,c2 = 0,0
        for chr in "aeiouAEIOU":
            if chr in cnt1:
                c1 +=cnt1[chr]
            if chr in cnt2:
                c2 +=cnt2[chr]
        return c1 == c2
