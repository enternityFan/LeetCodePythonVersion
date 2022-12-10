#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6261. 数组中字符串的最大值.py
@Author ：HuntingGame
@Date ：2022-12-10 22:39 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0

        for each in strs:
            flag = 0
            for i in range(26):
                if chr(ord('a') + i) in each:
                    flag = 1
                    break
            if not flag:
                ans = max(ans,eval(each))
            else:
                ans = max(ans,len(each))

        return ans
