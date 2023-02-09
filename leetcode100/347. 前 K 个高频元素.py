#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：347. 前 K 个高频元素.py
@Author ：HuntingGame
@Date ：2023-02-09 20:35 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        堆。时间复杂度是O(NlogK)的；如果是排序的话，得O(NlogN)的。
        首先做一个词频表。
        然后做一个大小为k的小根堆。
        :param nums:
        :param k:
        :return:
        """
        #TODO
        #其实就是要自己实现一个堆吧，然后堆里面的每个元素需要有词频和值。
        #72力扣二十四的1h12min