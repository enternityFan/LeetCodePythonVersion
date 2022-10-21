#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:24
# @Author  : HuntingGame
# @FileName: 1817. 查找用户活跃分钟数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        mydict = {}
        for each in logs:
            if each[0] not in mydict:
                mydict[each[0]] = set()
            mydict[each[0]].add(each[1])
        for key,val in mydict.items():
            ans[len(val)-1] +=1

        return ans
