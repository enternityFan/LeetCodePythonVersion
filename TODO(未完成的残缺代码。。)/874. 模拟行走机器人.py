#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 19:47
# @Author  : HuntingGame
# @FileName: 874. 模拟行走机器人.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:


        ans = 0
        x,y = 0,0
        flag = 1
        mydict = {1:[0,1],2:[-1,0],3:[0,-1],4:[1,0]} # 北 西 南 东
        cx,cy = mydict[flag]

        obstaclesx = sorted(obstacles,key=lambda x:x[0])
        obstaclesy = sorted(obstacles,key=lambda x:x[1])
        idx = 0
        idy = 0
        for i in range(len(commands)):
            if commands[i] =="-2":
                flag = (4 + flag - 1) % 4
                cx,cy = mydict[flag]
            elif commands[i] == "-1":
                flag = (4 + flag + 1) % 4
                cx,cy = mydict[flag]
            else:
                if flag == 1 or flag== 3:
                #x +=cx * commands[i]
                    y +=cy * commands[i]



