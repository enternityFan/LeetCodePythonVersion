# @Time : 2022-08-19 10:18
# @Author : Phalange
# @File : 1450. 在既定时间做作业的学生人数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        n = len(startTime)
        for i in range(n):
            if queryTime >= startTime[i] and queryTime <=endTime[i]:
                cnt +=1
        return cnt
