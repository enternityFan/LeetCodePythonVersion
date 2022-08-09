# @Time : 2022-08-09 21:34
# @Author : Phalange
# @File : 剑指 Offer II 105. 岛屿的最大面积.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 初始化
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.nodes[i*n + j] = i*n + j
                    self.parents[i*n + j] = i*n + j
                    self.sizeMap[i*n + j] = 1

        # 进行并查的操作
        for i in range(m):
            for j in range(n):
                if i+1 <m and grid[i][j] == 1 and grid[i+1][j] == 1:
                    self.union(i*n+j,(i+1)*n+j)

                if j+1<n and grid[i][j] == 1 and grid[i][j+1] == 1:
                    self.union(i*n+j,i*n + j+ 1)
        if self.sizeMap == {}:
            return 0
        return max(self.sizeMap.items(),key=lambda x:x[1])[1]



    def findFather(self,cur):
        path = []
        while cur !=self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        while path:
            self.parents[path.pop()] = cur

        return cur




    def isSameSet(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return False

        return self.findFather(self.nodes[a]) == self.findFather(self.nodes[b])




    def union(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSetSize = self.sizeMap[aHead]
            bSetSize = self.sizeMap[bHead]
            big = aHead if aSetSize >=bSetSize else bHead
            small = bHead if big == aHead else aHead
            self.sizeMap[big] = aSetSize + bSetSize
            self.parents[small] = big
            self.sizeMap.pop(small)



