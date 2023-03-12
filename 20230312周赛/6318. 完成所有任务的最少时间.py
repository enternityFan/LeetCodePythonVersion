#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6318. 完成所有任务的最少时间.py
@Author ：HuntingGame
@Date ：2023-03-12 10:43 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """
        [1,2,2,2,2]
        [1,2,2,2,3,3]
        :param tasks:
        :return:
        """
        cnts = [0] * 2001 #记录每个整点出现的次数
        tasks.sort(key=lambda x:(x[2],x[0]),reverse=True)
        print(tasks)
        ans = tasks[0][2]
        usedTime = [0] * 2001#0位置不用
        for i in range(tasks[0][0],tasks[0][1]+1):
            usedTime[i] +=ans
        for i in range(len(tasks)):
            for j in range(tasks[i][0],tasks[i][1]+1):
                cnts[j] +=1
        print(cnts)
        for i in range(1,len(tasks)):
            # 可能1，任务i完全落在了usedTime里面
            if usedTime[tasks[i][0]] !=0 and usedTime[tasks[i][1]] !=0:
                continue #完成这个任务，不需要额外的花销
            # 可能2，任务i的完成任务的段落在了usedTime里面
            elif usedTime[tasks[i][0]] !=0 and (tasks[i][0] + tasks[i][2]-1 < len(usedTime) and usedTime[tasks[i][0] + tasks[i][2]-1]!=0):
                continue
            elif usedTime[tasks[i][1]] !=0 and (tasks[i][1] - tasks[i][2]-1>0 and  usedTime[tasks[i][1] - tasks[i][0]-1]!=0):
                continue
            # 可能性3，需要额外的消耗，这个时

        return ans

tasks = [[1,3,2],[2,5,3],[5,6,2]]
print(Solution().findMinimumTime(tasks))