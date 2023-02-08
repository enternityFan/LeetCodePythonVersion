#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：210. 课程表 II.py
@Author ：HuntingGame
@Date ：2023-02-08 10:01 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List

class Node:
    def __init__(self, n):
        self.name = n
        self.innum = 0
        self.nexts = []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        这个题其实和207比，就是把拓扑排序的顺序给返回了。
        :param numCourses:
        :param prerequisites:
        :return:
        """

        ans = [0] * numCourses
        for i in range(numCourses):
            ans[i] = i
        if prerequisites is None or len(prerequisites) == 0:
            return ans
        nodes = {}#只记录了有依赖关系的课
        for arr in prerequisites:
            # arr就是依赖关系。
            to = arr[0]
            from_node = arr[1]
            if to not in nodes:
                nodes[to] = Node(to)
            if from_node not in nodes:
                nodes[from_node] = Node(from_node)

            t = nodes[to]
            f = nodes[from_node]
            f.nexts.append(t)
            t.innum += 1

        needPrerequisiteNums = len(nodes.keys())
        zeroInQueue = collections.deque()
        idx = 0
        for i in range(numCourses):
            if i not in nodes:
                ans[idx] = i
                idx +=1
            else:
                if nodes[i].innum == 0:  # 有依赖关系的课并且入度为0，是起始的节点
                    zeroInQueue.append(nodes[i])

        cnt = 0
        while len(zeroInQueue) != 0:
            cur = zeroInQueue.pop()
            ans[idx] = cur.name
            idx +=1
            cnt += 1
            for node in cur.nexts:
                node.innum -= 1

                if (node.innum == 0):
                    zeroInQueue.append(node)
        #如果不相等，说明不是所有的课都可以从队列里弹出，也就是说有循环依赖的。
        return ans if cnt == needPrerequisiteNums else [0]