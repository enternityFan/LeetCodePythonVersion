#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：49. 字母异位词分组.py
@Author ：HuntingGame
@Date ：2023-02-03 9:40 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        把str1和str2排序，如果一样，那就说明他们是。
        可以建立一个map,key是字符串排完序后的，value是一个列表，是排完序都是这个的。
        :param strs:
        :return:
        """
        mymap = {}
        for each in strs:
            str_s = "".join(sorted(each))
            if str_s not in mymap:
                mymap[str_s] = []
            mymap[str_s].append(each)
        ans = []
        for key,val in mymap.items():
            ans.append(val)
        return ans