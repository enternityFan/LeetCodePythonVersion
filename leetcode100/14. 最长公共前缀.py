#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：14. 最长公共前缀.py
@Author ：HuntingGame
@Date ：2023-02-01 18:46 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        思路很简单，把第一个字符串拿出来，然后遍历其他的每一个字符串，遍历到不一样就break
        :param strs:
        :return:
        """
        if len(strs) == 0:
            return ""

        chs = strs[0]
        ans = 10000000
        for each in strs:
            idx = 0
            while (idx < len(each) and idx < len(chs)):
                if each[idx] != chs[idx]:
                    break
                idx += 1
            ans = min(ans, idx)
            if ans == 0:
                return ""

        return chs[:ans]


