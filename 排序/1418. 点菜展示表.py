#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1418. 点菜展示表.py
@Author ：HuntingGame
@Date ：2023-03-12 12:33 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = []
        ids = []
        set_foods = set()
        set_ids = set()
        for order in orders:
            foods.append(order[2])
            ids.append(order[1])
            set_foods.add(order[2])
            set_ids.add(order[1])
        set_ids = list(set_ids)
        set_ids.sort(key=lambda x:int(x))
        set_foods = list(set_foods)
        set_foods.sort()
        food2id = {}
        for i in range(len(set_foods)):
            food2id[set_foods[i]] = i
        ids2id = {}
        for i in range(len(set_ids)):
            ids2id[set_ids[i]] = i
        ans = []
        ans.append(["Table"] + set_foods)
        ids,foods = zip(*sorted(zip(ids,foods),key=lambda x:x[0]))
        print(set_ids)
        for i in range(len(set_ids)):
            temp = [set_ids[i]] + ["0"] * len(set_foods)
            ans.append(temp)
        for i in range(len(ids)):
            ans[ids2id[ids[i]]+1][food2id[foods[i]]+1] = str(int(ans[ids2id[ids[i]]+1][food2id[foods[i]]+1])+1)

        return ans

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(Solution().displayTable(orders))