#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2517. 礼盒的最大甜蜜度.py
@Author ：HuntingGame
@Date ：2023-02-07 22:16 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        #[1,2,5,8,13,21]--->[1,3,3,5,7]这个是i与I-1的绝对值的差值
        #肯定是从后往前选
        #TODO