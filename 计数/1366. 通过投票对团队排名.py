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
        if len(votes)==1:
            return votes[0]
        paixu = [[0] * len(votes[0]) for i in range(len(votes[0]))]
        team = [c for c in votes[0]]
        team.sort()
        mydict = {}
        for i in range(len(team)):
            mydict[team[i]] = i


        for i in range(len(votes)):
            for j in range(len(votes[i])):
                paixu[mydict[votes[i][j]]][j] +=1


        team,paixu = zip(*sorted(zip(team,paixu),key=lambda x:(x[1],-ord(x[0])),reverse=True))
        print(paixu)
        return "".join(team)
votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
votes = ["WXYZ","XYZW"]
print(Solution().rankTeams(votes))





