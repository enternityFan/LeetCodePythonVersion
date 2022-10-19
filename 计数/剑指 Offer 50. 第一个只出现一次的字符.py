#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 50. 第一个只出现一次的字符.py
@Author ：HuntingGame
@Date ：2022-10-18 12:32 
C'est la vie!!! enjoy ur day :D
'''
import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return " "
        first = [60000] * 26
        flag = 0
        mydict = collections.Counter(s)
        for key, val in mydict.items():
            if val == 1:
                first[ord(key) - ord('a')] = s.find(key)
                flag = 1
        if flag == 0 :
            return " "

        return s[min(first)]

print(Solution().firstUniqChar("cc"))

