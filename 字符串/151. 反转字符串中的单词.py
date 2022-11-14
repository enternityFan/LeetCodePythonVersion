#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：151. 反转字符串中的单词.py
@Author ：HuntingGame
@Date ：2022-11-14 10:37 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))