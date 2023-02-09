#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：326. 3 的幂.py
@Author ：HuntingGame
@Date ：2023-02-09 14:14 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        如果n只含3这个因子，那他就是3的幂，那他一定能被int下最大的3的幂，3 ** 19次方取模为0
        :param n:
        :return:
        """


        return ( n > 0 and 1162261467 % n == 0)