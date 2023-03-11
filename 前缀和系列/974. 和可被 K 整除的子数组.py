#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：974. 和可被 K 整除的子数组.py
@Author ：HuntingGame
@Date ：2023-03-11 19:10 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        利用了同余的性质：a % x = c,并且 b % x = c,那么（a-b) %x = 0
        :param nums:
        :param k:
        :return:
        """
        mydict = {0:1}#模为0的数有1个，这个初始化是考虑前缀和本身被k整除的边界情况
        total,ans = 0,0
        for each in nums:
            total +=each
            mod = total % k
            same = mydict.get(mod,0)
            ans +=same
            mydict[mod] = same + 1


        return ans




