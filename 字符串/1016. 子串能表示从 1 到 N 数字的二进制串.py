#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1016. 子串能表示从 1 到 N 数字的二进制串.py
@Author ：HuntingGame
@Date ：2022-11-14 10:07 
C'est la vie!!! enjoy ur day :D
'''
import collections


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        cnt1 = collections.Counter(s)
        one = 0
        zero = 0
        for i in range(1,n+1):
            tmp = 1
            tmpstr = ""
            while tmp <=i:
                if i & tmp == tmp:
                    tmpstr = "1" + tmpstr
                else:
                    tmpstr = "0" + tmpstr
                tmp <<=1

            if s.find(tmpstr) == -1:
                return False
        return True



print(Solution().queryString("0110",3))