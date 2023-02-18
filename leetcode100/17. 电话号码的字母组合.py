#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：17. 电话号码的字母组合.py
@Author ：HuntingGame
@Date ：2023-02-01 20:32 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []


        ans = []
        path = [0] * len(digits)

        self.process(digits,0,path,ans)

        return ans

    def process(self,s,idx,path,ans):
        if idx == len(s):
            ans.append("".join(path))
            return
        cands = self.phone[s[idx]]
        for cur in cands:
            path[idx] = cur
            self.process(s,idx+1,path,ans)

