# @Time : 2022-10-11 20:52
# @Author : Phalange
# @File : 2432. 处理用时最长的那个任务的员工.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longidx = logs[0][0]
        longtime = logs[0][1]
        for i in range(1,len(logs)):
            if longtime < logs[i][1] - logs[i-1][1]:
                longidx = logs[i][0]
                longtime = logs[i][1] - logs[i-1][1]
            elif longtime == logs[i][1] - logs[i-1][1]:
                longidx = min(longidx,logs[i][0])

        return longidx
n = 10
logs = [[0,3],[2,5],[0,9],[1,15]]
print(Solution().hardestWorker(n,logs))
