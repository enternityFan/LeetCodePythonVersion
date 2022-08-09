# @Time : 2022-08-09 19:57
# @Author : Phalange
# @File : 547. 省份数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()



    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # 初始化并查集
        for i in range(len(isConnected)):
            self.nodes[i] = i
            self.parents[i] = i
            self.sizeMap[i] = 1
        # 根据连接表建立并查集
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:

                    # 两个省相连接
                    #print(i,j)

                    self.union(i,j)

        return len(self.sizeMap)





    def findFather(self,cur):
        path =[]
        while cur !=self.parents[cur] :
            path.append(cur)
            cur = self.parents[cur]

        #cur当前为头结点
        while path:
            self.parents[path.pop()] = cur #做了一个扁平的优化的操作

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
        if aHead !=bHead:
            aSetSize = self.sizeMap[aHead]
            bSetSize = self.sizeMap[bHead]
            big = aHead if aSetSize >= bSetSize else bHead
            small = bHead if big == aHead else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSetSize + bSetSize
            self.sizeMap.pop(small)


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
print(Solution().findCircleNum(isConnected))