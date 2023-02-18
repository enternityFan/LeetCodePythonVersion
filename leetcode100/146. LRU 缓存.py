#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：146. LRU 缓存.py
@Author ：HuntingGame
@Date ：2023-02-06 11:34 
C'est la vie!!! enjoy ur day :D
'''

class MyCache:
    def __init__(self,capacity):
        self.capacity = capacity
        keyNodeMap = {}



class LRUCache:

    def __init__(self, capacity: int):
        """
        map记录节点内存地址就可以不在双向链表里面遍历了的。
        :param capacity:
        """
        self.cache = MyCache(capacity)
        #TODO 这个代码没学。


    def get(self, key: int) -> int:
        ans = self.cache.get(key)
        return -1 if ans is None else ans


    def put(self, key: int, value: int) -> None:
        self.cache.set(key,value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)