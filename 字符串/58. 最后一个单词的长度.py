#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：58. 最后一个单词的长度.py
@Author ：HuntingGame
@Date ：2022-10-20 9:37 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(" ")
        s = s.lstrip(" ")
        s = s.split(" ")
        return len(s[-1])