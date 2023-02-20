#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 12:24
# @Author  : HuntingGame
# @FileName: 2347. 最好的扑克手牌.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cnt_ranks = collections.Counter(ranks)
        cnt_suits = collections.Counter(suits)
        for key,val in cnt_suits.items():
            if val  == 5:
                return "Flush"

        for key,val in cnt_ranks.items():
            if val == 3:
                return "Three of a Kind"

        for key,val in cnt_ranks.items():
            if val == 2:
                return "Pair"

        return "High Card"
