#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：1207. 独一无二的出现次数.py
@Author ：HuntingGame
@Date ：2022/9/22 8:37 
C'est la vie!!! :)
'''
import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydict = collections.Counter(arr)
        myset = set()
        for key,val in mydict.items():
            if val not in myset:
                myset.add(val)
            else:
                return False

        return True
