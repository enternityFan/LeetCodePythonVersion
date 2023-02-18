#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：207. 课程表.py
@Author ：HuntingGame
@Date ：2023-02-08 9:34 
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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        这个代码也是标准的拓扑排序J
        这个题就是拓扑排序。如果能排就返回True，不能就是False
        这个讲解在并查集结构和图相关的算法里面的。
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if prerequisites is None or len(prerequisites) == 0:
            return True
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
        for node in nodes.values():
            if node.innum == 0:  # 有依赖关系的课并且入度为0，是起始的节点
                zeroInQueue.append(node)

        cnt = 0
        while len(zeroInQueue) != 0:
            cur = zeroInQueue.pop()
            cnt += 1
            for node in cur.nexts:
                node.innum -= 1

                if (node.innum == 0):
                    zeroInQueue.append(node)
        #如果不相等，说明不是所有的课都可以从队列里弹出，也就是说有循环依赖的。
        return cnt == needPrerequisiteNums