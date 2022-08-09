# @Time : 2022-08-09 16:16
# @Author : Phalange
# @File : 797. 所有可能的路径.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = list()
        tmp = list()
        def dfs(x:int):
            if x == len(graph) - 1:
                ans.append(tmp[:])# 用[:]表示重新分配了内存给新的列表变量
                return

            for y in graph[x]:
                tmp.append(y)
                dfs(y)
                tmp.pop()
        tmp.append(0)
        dfs(0)
        return ans