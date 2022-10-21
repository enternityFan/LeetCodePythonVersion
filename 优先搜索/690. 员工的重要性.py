#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 18:14
# @Author  : HuntingGame
# @FileName: 690. 员工的重要性.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:

    def __init__(self):
        self.ans = 0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance_dict = {}
        subordinates_dict = {}
        for each in employees:
            importance_dict[each.id] = each.importance
            subordinates_dict[each.id] = each.subordinates

        def dfs(id):
            for each in subordinates_dict[id]:
                print(each)
                self.ans +=importance_dict[each]
                if subordinates_dict[id] ==[]:
                    continue
                dfs(each)

        dfs(id)
        return self.ans+importance_dict[id]
