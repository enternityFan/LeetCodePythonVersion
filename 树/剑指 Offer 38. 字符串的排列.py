#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 38. 字符串的排列.py
@Author ：HuntingGame
@Date ：2023-03-06 18:58 
C'est la vie!!! enjoy ur day :D
'''
import copy
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
    def permutation(self, s: str) -> List[str]:
        ls = [c for c in s]
        self.process(ls,0)
        return list(set(self.ans))

    def process(self,s,i):
        if i == len(s)-1:
            self.ans.append("".join(s))
            return

        for j in range(i,len(s)):
            s[i],s[j] = s[j],s[i]

            self.process(s,i+1)
            s[i], s[j] = s[j], s[i]

print(Solution().permutation("abc"))