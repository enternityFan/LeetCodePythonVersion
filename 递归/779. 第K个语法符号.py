#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：779. 第K个语法符号.py
@Author ：HuntingGame
@Date ：2022-10-20 8:33 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        假设f(n,k)是第n行第k个元素
        如果k小于 f(n-1)的长度，那么f(n,k) = f(n-1,k)
        如果k大于f(n-1)的长度，那么f(n,k) = ~f(n-1,k),~为位运算的取反
        :param n:
        :param k:
        :return:
        """
        if n == 1:
            if k <= 2 ** (n-1):
                return 0
            else:
                return 1
        if k <= 2 ** (n-1):
            return self.kthGrammar(n-1,k)
        else:
            return 1 - self.kthGrammar(n-1,k-2 ** (n-1))

print(Solution().kthGrammar(4,2))



