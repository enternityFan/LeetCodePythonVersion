#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：191. 位1的个数.py
@Author ：HuntingGame
@Date ：2023-02-07 21:09 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        rightOne = 0
        while n !=0:
            rightOne = n & (-n) #提取最右侧的1
            n ^=rightOne #去掉最后一个n
            bits +=1
        return bits
