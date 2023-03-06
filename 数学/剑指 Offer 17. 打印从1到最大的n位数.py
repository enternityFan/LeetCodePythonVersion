#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 17. 打印从1到最大的n位数.py
@Author ：HuntingGame
@Date ：2023-03-06 18:40 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1,10 ** n))