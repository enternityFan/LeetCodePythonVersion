#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：5. 最长回文子串.py
@Author ：HuntingGame
@Date ：2023-02-01 12:02 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #TODO
        # Manacher算法
        n = len(s)