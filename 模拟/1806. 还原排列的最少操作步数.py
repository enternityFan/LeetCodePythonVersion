#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1806. 还原排列的最少操作步数.py
@Author ：HuntingGame
@Date ：2022-10-25 9:08 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        ops = 0
        flag = 0
        n_2 = n // 2
        while not flag:
            arr = [0] * n
            flag2 = 0
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n_2 + (i-1) // 2]
                if arr[i] == i:
                    flag2 +=1
            ops +=1
            perm = arr.copy()
            if flag2 == n:
                flag = 1




        return ops