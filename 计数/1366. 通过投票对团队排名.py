#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 18:22
# @Author  : HuntingGame
# @FileName: 1366. 通过投票对团队排名.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        team = [0] * 26
        paixu = list(range(26))
        for i in range(len(votes)):
            for j in range(len(votes[i])):
                team[ord(votes[i][j]) - ord('A')] +=1





