#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 21:30
# @Author  : HuntingGame
# @FileName: 2410. 运动员和训练师的最大匹配数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        j = 0
        for i in range(len(players)):
            while j < len(trainers):
                if players[i] <= trainers[j]:
                    ans +=1
                    j +=1
                    break
                j +=1
            if j == len(trainers):
                break
        return ans