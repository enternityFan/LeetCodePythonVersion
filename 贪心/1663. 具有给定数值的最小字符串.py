#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1663. 具有给定数值的最小字符串.py
@Author ：HuntingGame
@Date ：2022-11-01 9:23 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        ans = []
        while k:
            if k >26:
                for i in range(26,0,-1):
                    if k - i >= n-1:
                        k = k - i
                        n -=1
                        ans.append(chr(ord('a') + i))
            else:
                # 填最小的
                if n == 1:
                    ans.append(chr(ord('a') + k))
                    break
                for i in range(1,27):
                    if k -i >= n-1:
                        k = k - i
                        n -=1
                        ans.append(chr(ord('a') + i))
        return "".join(sorted(ans))

print(Solution().getSmallestString(3,27))