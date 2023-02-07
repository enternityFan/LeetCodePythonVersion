#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：204. 计数质数.py
@Author ：HuntingGame
@Date ：2023-02-07 21:31 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def countPrimes(self, n: int) -> int:

        f = [False] * n
        cnt = n // 2
        i = 3
        while i * i < n:
            if f[i]:
                continue
            j = i * i
            while j < n:
                if not f[j]:
                    cnt -=1
                    f[j] = True



                j +=2*i


            i +=2
        return cnt
