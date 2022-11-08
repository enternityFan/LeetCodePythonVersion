#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2109. 向字符串添加空格.py
@Author ：HuntingGame
@Date ：2022-11-07 9:30 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        for i in range(len(s)):

            if j < len(spaces) and i == spaces[j]:
                j+=1
                ans +=" "
            ans +=s[i]

        return ans

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(Solution().addSpaces(s,spaces))