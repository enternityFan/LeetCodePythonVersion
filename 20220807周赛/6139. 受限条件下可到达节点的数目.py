# @Time : 2022-08-07 10:34
# @Author : Phalange
# @File : 6139. 受限条件下可到达节点的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def __init__(self):
        self.mpath = collections.defaultdict(list)
        self.allPath = [[0]]
        self.nodes = set([0])
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def func(cur):
            if cur == []:
                return
            for each in cur:
                if each in self.nodes or each in restricted:
                    continue
                self.allPath[-1].append(each)
                self.nodes.add(each)
                func(self.mpath[each])

        for i in range(n-1):

            #if edges[i][0] not in restricted or edges[i][1] not in restricted:
            self.mpath[edges[i][0]].append(edges[i][1])
            self.mpath[edges[i][1]].append(edges[i][0])

        #return len(nodes) if len(nodes) !=0 else 1
        cur = self.mpath[0]
        while cur !=[]:
            # 把路串一下
            for each in cur:
                if each in self.nodes or each in restricted:
                    continue
                self.allPath.append([0,each])
                self.nodes.add(each)
                func(self.mpath[each])
            break
        #return len(self.nodes)
        return self.allPath,self.mpath
n = 7
edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
restricted = [4,2,1]
n = 10
edges = [[8,2],[2,5],[5,0],[2,7],[1,7],[3,8],[0,4],[3,9],[1,6]]
restricted = [9,8,4,5,3,1]
# n = 10
# edges = [[4,1],[1,3],[1,5],[0,5],[3,6],[8,4],[5,7],[6,9],[3,2]]
# restricted = [2,7]
print(Solution().reachableNodes(n,edges,restricted))




