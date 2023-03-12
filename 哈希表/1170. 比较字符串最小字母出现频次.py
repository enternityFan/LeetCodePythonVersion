#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1170. 比较字符串最小字母出现频次.py
@Author ：HuntingGame
@Date ：2023-03-12 11:06 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        ans = []
        aim = self.f(words)
        for i in range(len(queries)):
            tmp = self.f(queries[i])
            ans.append()


        return ans

    def f(self,s):
        s.sort()
        ans = 1
        for i in range(1,len(s)):
            if s[i] !=s[i-1]:
                break
            ans +=1
        return ans







