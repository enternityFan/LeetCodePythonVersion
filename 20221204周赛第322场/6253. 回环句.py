#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6253. 回环句.py
@Author ：HuntingGame
@Date ：2022-12-04 10:30 
C'est la vie!!! enjoy ur day :D
'''



class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        n = len(sentence)
        if n == 1:
            return sentence[0][-1] == sentence[0][0]

        for i in range(1,n):
            if sentence[i-1][-1] !=sentence[i][0]:
                return False



        return sentence[0][0] == sentence[-1][-1]

print(Solution().isCircularSentence("leetcode"))