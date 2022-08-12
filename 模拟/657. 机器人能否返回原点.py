# @Time : 2022-08-11 21:24
# @Author : Phalange
# @File : 657. 机器人能否返回原点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mydict = collections.defaultdict(int)
        for c in moves:
            mydict[c] +=1

        if mydict['R'] == mydict['L'] and mydict['U'] == mydict['D']:
            return True
        return False
