#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 20:25
# @Author  : HuntingGame
# @FileName: 1170. 比较字符串最小字母出现频次.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        for i in range(len(queries)):
            cnt1[ self.f(queries[i])] +=1

        for j in range(len(words)):
            cnt2[self.f(words[j])] +=1







    def f(self,s):
        s = sorted(s)

        ans = 0
        prev = None
        if len(s) == 1:
            return 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                ans +=1
            else:
                break
        return ans
