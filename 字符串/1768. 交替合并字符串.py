#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 8:48
# @Author  : HuntingGame
# @FileName: 1768. 交替合并字符串.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        ans = ""
        while p1 < len(word1) and p2 < len(word2):
            ans +=word1[p1]
            ans +=word2[p2]
            p1 +=1
            p2 +=1
        while p1 < len(word1):
            ans +=word1[p1]
            p1 +=1
        while p2 < len(word2):
            ans +=word2[p2]
            p2 +=1
        return ans
