#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：677. 键值映射.py
@Author ：HuntingGame
@Date ：2022-11-08 9:05 
C'est la vie!!! enjoy ur day :D
'''
class MapSum:

    def __init__(self):
        self.mydict = {}

    def insert(self, key: str, val: int) -> None:
        self.mydict[key] = val




    def sum(self, prefix: str) -> int:
        ans = 0
        for key,val in self.mydict.items():
            if prefix == key[:len(prefix)]:
                ans +=val

        return ans







# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)