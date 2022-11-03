#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1668. 最大重复子字符串.py
@Author ：HuntingGame
@Date ：2022-11-03 8:57 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        idx = sequence.find(word)
        while idx !=-1:
            k+=1
            word = word + word
            idx = sequence.find(word)

        return k