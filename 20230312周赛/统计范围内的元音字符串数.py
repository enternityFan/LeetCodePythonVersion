#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：统计范围内的元音字符串数.py
@Author ：HuntingGame
@Date ：2023-03-12 10:30 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        ans = 0
        for i in range(left,right+1):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                ans +=1
        return ans