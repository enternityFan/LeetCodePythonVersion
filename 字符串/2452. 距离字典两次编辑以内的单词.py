#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2452. 距离字典两次编辑以内的单词.py
@Author ：HuntingGame
@Date ：2022-11-08 8:38 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for i in range(len(queries)):

            for j in range(len(dictionary)):
                cnt = 0
                for k in range(len(queries[i])):
                    if queries[i][k] !=dictionary[j][k]:
                        cnt +=1
                        if cnt ==3:
                            break
                if cnt <=2:
                    ans.append(queries[i])
                    break


        return ans


