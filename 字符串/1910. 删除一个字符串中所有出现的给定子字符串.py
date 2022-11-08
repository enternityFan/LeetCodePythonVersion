#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1910. 删除一个字符串中所有出现的给定子字符串.py
@Author ：HuntingGame
@Date ：2022-11-08 8:07 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        idx = s.find(part)
        prev_idx = -1
        while idx !=-1:

            s = s[:idx] + s[idx+len(part):]

            idx =  s.find(part)
        return s

print(Solution().removeOccurrences("daabcbaabcbc","abc"))




