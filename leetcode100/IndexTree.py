#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：IndexTree.py
@Author ：HuntingGame
@Date ：2023-02-09 13:52 
C'est la vie!!! enjoy ur day :D
'''


# 1维IndexTree
class IndexTree:
    def __init__(self,size):
        self.tree = [0] * (size+1)
        self.N = size

    def sum(self,idx):
        """
        返回0.。。idx范围的累加和
        :param idx:
        :return:
        """
        ret = 0
        while idx > 0:
            ret +=self.tree[idx]
            idx -=idx & -idx #提取数的二进制 最后的1

        return ret

    def add(self,idx,d):
        """
        idx位置的数增加了d，对应的其他位置进行更新。
        :param idx:
        :param d:
        :return:
        """
        while idx <=self.N:
            self.tree[idx] +=d
            idx += idx & -idx

