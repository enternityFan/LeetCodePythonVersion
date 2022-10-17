#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 10:00
# @Author  : HuntingGame
# @FileName: 面试题 16.10. 生存人数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List







class Solution2:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        cnts = [0] * 101
        for i in range(len(birth)):
            for j in range(birth[i],death[i]+1):
                cnts[j-1900] +=1
        maxval = max(cnts)
        return cnts.index(maxval)+1900

birth = [1900, 1901, 1950]
death = [1948, 1951, 2000]
print(Solution().maxAliveYear(birth,death))