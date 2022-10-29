#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2068. 检查两个字符串是否几乎相等.py
@Author ：HuntingGame
@Date ：2022-10-27 18:34 
C'est la vie!!! enjoy ur day :D
'''
import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        flag = 1
        for key,val in cnt1.items():
            if key not in word2 and val >3:
                return False
            elif key in word2 and abs(val - word2[key]) >3:
                return False
        for key,val in cnt2.items():
            if key not in word1 and val >3:
                return False



        return flag


