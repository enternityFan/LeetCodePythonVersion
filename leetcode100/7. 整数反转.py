#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：7. 整数反转.py
@Author ：HuntingGame
@Date ：2023-02-01 12:06 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def reverse(self, x: int) -> int:
        # 首先取出来符号位
        neg = ((x >> 31) & 1) == 1
        x = x if neg == 1 else -x# 都当做负数来处理，因为负数所能表达的域更大。
        minval = (-2 ** 31) // 10
        maxval = (-2 ** 31) % 10
        res = 0
        while x!=0:
            if res < minval or (res == minval and x % 10 < maxval):
                # 防止溢出的。
                return 0
            digit = x % 10
            if x < 0 and digit > 0:
                digit -=10
            res = res*10 +digit
            x =(x-digit) // 10
        if res > 2**31 - 1 or res < -2**31:
            return 0
        return res if neg else abs(res)

print(Solution().reverse(1563847412))