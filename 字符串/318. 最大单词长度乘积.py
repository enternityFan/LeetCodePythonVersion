#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：318. 最大单词长度乘积.py
@Author ：HuntingGame
@Date ：2022-11-08 9:19 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        words2 = [0] * len(words)
        for i in range(len(words)):

            for c in words[i]:
                words2[i] |= (1 << (ord(c) - ord('a')))

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words2[i] & words2[j] == 0:
                    ans = max(ans,len(words[i]) * len(words[j]))

        return ans
