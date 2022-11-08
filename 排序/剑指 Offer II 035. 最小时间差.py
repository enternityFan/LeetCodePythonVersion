#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 035. 最小时间差.py
@Author ：HuntingGame
@Date ：2022-11-08 8:24 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        """

        都把转换为他们的分钟表示，然后找最小的绝对值差
        :param timePoints:
        :return:
        """
        time = []
        for i in range(len(timePoints)):
            h,m = timePoints[i].split(":")
            time.append(int(h) * 60 + int(m))
        time.sort()
        ans = 10000000
        for i in range(len(time)):
            if i == len(time)-1:
                print(abs(time[0] - time[-1]))
                print(abs(1440 - time[-1] + time[0]))
                ans = min(ans,min(abs(time[0]-time[-1]),abs(1440 - time[-1] +time[0])))
            else:
                ans = min(ans,abs(time[i] - time[i+1]))
            if ans == 0:
                break
        return ans

timePoints = ["12:12","00:13"]

print(Solution().findMinDifference(timePoints))



