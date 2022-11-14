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
            if key == 0:
                ans +=val
                continue
            if val <=key+1: # key=1,val=2,val=1
                ans +=key + 1
            else:# key=1,val = 3 很明显需要4个兔子起码
                if val %(key+1) == 0:
                    ans += (key + 1) * (val // (key+1))

                else:

                    ans += (key + 1) * (val // (key + 1)) + (key + 1)
        return ans


print(Solution().numRabbits([0,1,0,2,0,1,0,2,1,1]))