#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 10:30
# @Author  : HuntingGame
# @FileName: 6214. 判断两个事件是否存在冲突.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        time1s = int(event1[0].split(":")[0]) * 60 + int(event1[0].split(":")[1])
        time1e = int(event1[1].split(":")[0]) * 60 + int(event1[1].split(":")[1])
        time2s = int(event2[0].split(":")[0]) * 60 + int(event2[0].split(":")[1])
        time2e = int(event2[1].split(":")[0]) * 60 + int(event2[1].split(":")[1])
        print(time1s,time1e,time2s,time2e)
        if (time2s >=time1s and time2s <= time1e) or (time1s >=time2s and time1s <= time2e):
            return True

        return False
event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
print(Solution().haveConflict(event1,event2))
