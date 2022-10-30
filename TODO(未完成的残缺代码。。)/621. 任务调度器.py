#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 16:05
# @Author  : HuntingGame
# @FileName: 621. 任务调度器.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = collections.Counter(tasks)
        print(cnts)
        if n == 0:
            return len(tasks)
        times = list(cnts.values())
        times.sort(reverse=True)
        mintime = times[0] + n * (times[0] -1)



        for i in range(1,len(times)):
            if times[i] == times[0]:
                mintime +=1
            else:
                break




        return mintime


tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks,n))