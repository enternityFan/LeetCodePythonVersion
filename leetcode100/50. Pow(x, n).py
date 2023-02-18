#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：50. Pow(x, n).py
@Author ：HuntingGame
@Date ：2023-02-03 9:49 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        logN
        快速幂。比如a^75,首先算一下75的二进制形式:1001011
        那么可以做一个t首先抓取a^1,那么t2=a^2,t3=a^3....t^6=64,
        那么res=1*a^1*a^2*a^8*a^64.这就比乘a乘75次少太多了。
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1.0
        if n == -2 ** 31:
            #只需要讨论x为正负1的情况，其他情况，要么溢出，要么为0.
            return 1.0 if x == 1.0 or x == -1.0 else 0
        pow = abs(n)
        t = x
        ans = 1.0
        while pow !=0:
            if pow & 1 !=0:
                ans *=t
            pow >>=1
            t = t * t

        return 1.0/ans if n < 0 else ans












