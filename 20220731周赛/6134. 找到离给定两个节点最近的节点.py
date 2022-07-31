# @Time : 2022-07-31 11:06
# @Author : Phalange
# @File : 6134. 找到离给定两个节点最近的节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node2 == node1:
            return node1
        # 找出所有的路径，包含node1和node2的
        roads = [] # [i]个[]是从这个点到其他点的完整路径
        for i in [node1,node2]:
            road = []
            road.append(i)
            value = edges[i]
            while value !=-1 : # 需要考虑环
                road.append(value)
                value = edges[value]
                if value in road:
                    road.append(value)
                    break
            roads.append(road)

        # 然后再找一下每个节点到这俩节点的距离和
        res = [[],[]]# 初始设置为0,i个位置表示这个位置到两个节点的距离和
        idx = -1 #答案
        minValue = 1e6

        for i in range(len(edges)):
            if i not in roads[0]:
                res[0].append(-1)
            else:
                res[0].append(roads[0].index(i))
            if i not in roads[1]:
                res[1].append(-1)
            else:
                res[1].append(roads[1].index(i))

            tmp = max(res[0][i],res[1][i]) if res[0][i] !=-1 and res[1][i] !=-1 else 1e6
            if tmp < minValue and tmp !=-1:
                idx = i
                minValue = tmp



        return idx

print(Solution().closestMeetingNode([1,2,3,2,5,4],4,1))
print(Solution().closestMeetingNode([-1,-1,-1,-1,-1],1,3))
print(Solution().closestMeetingNode([9,8,7,0,5,6,1,3,2,2],1,6))
print(Solution().closestMeetingNode([4,4,4,5,1,2,2],1,1))
print(Solution().closestMeetingNode([4,3,0,5,3,-1],4,0))
print(Solution().closestMeetingNode([2,2,3,-1],0,1))
print(Solution().closestMeetingNode([1,2,-1],0,2))