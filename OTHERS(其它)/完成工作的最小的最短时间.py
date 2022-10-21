#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 17:02
# @Author  : HuntingGame
# @FileName: 完成工作的最小的最短时间.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = 10000000
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        tmp = [0] * k
        # ans = math.inf
        jobs.sort(reverse=True)

        def process(idx):

            if idx == len(jobs):
                self.ans = min(self.ans, max(tmp))

                return

            # 判断是否不够分
            zcnt = 0
            for i in tmp:
                if i == 0: zcnt += 1
            if zcnt > len(jobs) - idx:
                return  # 这个方案不行
            for i in range(k):
                if tmp[i] > self.ans:
                    return  # 这个方案不行
            for i in range(k):
                tmp[i] += jobs[idx]
                process(idx + 1)
                tmp[i] -= jobs[idx]

        process(0)
        return self.ans
