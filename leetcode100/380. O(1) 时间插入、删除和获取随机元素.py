#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：380. O(1) 时间插入、删除和获取随机元素.py
@Author ：HuntingGame
@Date ：2023-02-09 21:12 
C'est la vie!!! enjoy ur day :D
'''
import random


class RandomizedSet:

    def __init__(self):
        """
        俩map，一
        """
        self.keyIndexmap = {}
        self.indexKeymap = {}
        self.size = 0


    def insert(self, val: int) -> bool:
        if val not in self.keyIndexmap:
            self.keyIndexmap[val] = self.size
            self.indexKeymap[self.size] = val
            self.size +=1
            return True

        return False


    def remove(self, val: int) -> bool:
        """
        思路就是把最后一个记录给拿出来，给他放到val位置的索引上，这样就把那个洞给填上了。
        :param val:
        :return:
        """
        if val in self.keyIndexmap:
            deleteIndex = self.keyIndexmap[val]
            self.size -=1
            lastIndex = self.size
            lastKey = self.indexKeymap[lastIndex]
            self.keyIndexmap[lastKey] = deleteIndex #重复利用的，
            self.indexKeymap[deleteIndex] = lastKey
            self.keyIndexmap.pop(val)
            self.indexKeymap.pop(lastIndex)
            return True
        return False

    def getRandom(self) -> int:
        if self.size == 0:
            return -1
        randomIndex = int(random.random() * self.size)
        return self.indexKeymap[randomIndex]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()