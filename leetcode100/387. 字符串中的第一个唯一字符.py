#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：387. 字符串中的第一个唯一字符.py
@Author ：HuntingGame
@Date ：2023-02-10 8:16 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnts = [0] * 256
        for i in range(len(s)):
            cnts[ord(s[i]) - ord('a')] +=1

        for i in range(len(s)):
            if cnts[ord(s[i]) - 'a'] == 1:
                return i
        return -1