#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1657. 确定两个字符串是否接近.py
@Author ：HuntingGame
@Date ：2022-11-14 10:40 
C'est la vie!!! enjoy ur day :D
'''
import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) !=len(word2):
            return False
        if set(word2) !=set(word1):
            return False
        word1 = "".join(sorted(word1))
        word2 = "".join(sorted(word2))
        if word1 == word2:
            return True
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)

        l1 = list(cnt1.values())
        l2 = list(cnt2.values())
        l1.sort()
        l2.sort()
        return l1 == l2

word1 = "abbzzca"

word2 = "babzzcz"

print(Solution().closeStrings(word1,word2))
