#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1003. 检查替换后的词是否有效.py
@Author ：HuntingGame
@Date ：2022-11-14 10:00 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def isValid(self, s: str) -> bool:

        idx = s.find("abc")
        while s and idx!=-1:

            s = s[:idx] + s[idx+3:]
            idx = s.find("abc")

        if idx == -1 and s !="":
            return False
        return True

print(Solution().isValid("aabcbc"))