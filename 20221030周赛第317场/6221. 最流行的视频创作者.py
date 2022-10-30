#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6221. 最流行的视频创作者.py
@Author ：HuntingGame
@Date ：2022-10-30 10:32 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        mydict = {}
        mydict2 = {}
        for i in range(n):
            if creators[i] not in mydict:
                mydict[creators[i]] = {}
            if creators[i] not in mydict2:
                mydict2[creators[i]] = 0
            mydict[creators[i]][ids[i]] = views[i]
            mydict2[creators[i]] +=views[i]

        max_creators = set()
        maxval = max(mydict2.values())
        for key,val in mydict2.items():
            if val == maxval:
                max_creators.add(key)
        ans = []
        for key,val in mydict.items():
            if key not in max_creators:
                continue
            tmpval = max(val.values())
            tmp = ""
            for key2,val2 in val.items():
                if val2 == tmpval:
                    if tmp == "" or tmp > key2:
                        tmp = key2

            ans.append([key,tmp])

        return ans
