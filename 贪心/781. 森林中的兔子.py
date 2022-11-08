#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：781. 森林中的兔子.py
@Author ：HuntingGame
@Date ：2022-11-08 9:30 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        myset = set()
        ans = 0

        cnts = collections.Counter(answers)
        for key,val in cnts.items():

            if val <=key:
                ans +=val + 1
            else:
                ans += (val // key) * key + (key - (val % key) + 1)

        return ans


print(Solution().numRabbits([1,1,2]))