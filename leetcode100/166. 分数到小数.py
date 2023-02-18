#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：166. 分数到小数.py
@Author ：HuntingGame
@Date ：2023-02-07 19:38 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        这个题的踩很多的，主要考coding
        思路就是，a/b = c ....d,然后对余数d * 10 / b = c2....d2,然后重复这样
        要用一个map记录一下小数点的位置，通过这个方式，就可以知道循环界在哪了
        确实，听起来这个思路挺难的也。。
        :param numerator:
        :param denominator:
        :return:
        """
        if numerator == 0:
            return '0'
        res = "-" if (numerator>0) ^ (denominator > 0) else ""
        num = abs(numerator)
        den = abs(denominator)
        res +=str(num // den)
        num %=den
        if num == 0:
            return res
        res +="."
        mymap = {}
        mymap[num] = len(res)
        while num !=0:
            num *=10
            res += str(num // den)
            num %=den
            if num in mymap:
                idx = mymap[num]
                res = res[:idx+1] + "(" + res[idx+1:]
                res +=")"
                break
            else:
                mymap[num] = len(res)

        return res

