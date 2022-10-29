#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 15:56
# @Author  : HuntingGame
# @FileName: 1400. 构造 K 个回文字符串.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        # s的长度>=k 并且 s中奇数字符的个数<=k即满足要求
        if len(s) == k:
            return True
        elif len(s) < k:
            return False
        scnt = collections.Counter(s)
        ans = 0
        for key,val in scnt.items():
            if val % 2 == 1:
                ans +=1
        return ans <=k


