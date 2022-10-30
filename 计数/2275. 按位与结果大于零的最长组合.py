#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 17:46
# @Author  : HuntingGame
# @FileName: 2275. 按位与结果大于零的最长组合.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        ans = [0] * 24 #24位，每一位存储第i个二进制位非零的长度

        for i in range(24):
            for j in range(len(candidates)):
                if (candidates[j] & (1 << i)) !=0:
                    ans[i] +=1

        print(ans)
        return max(ans)


candidates = [16,17,71,62,12,24,14]
print(Solution().largestCombination(candidates))
