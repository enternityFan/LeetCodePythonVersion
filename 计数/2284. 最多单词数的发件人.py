#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 17:57
# @Author  : HuntingGame
# @FileName: 2284. 最多单词数的发件人.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mydict = {}
        n = len(messages)
        for i in range(n):
            if senders[i] not in mydict:
                mydict[senders[i]] = 0
            mydict[senders[i]] +=len(messages[i].split(" "))

        maxkey = ""
        maxval = -1
        for key,val in mydict.items():
            if val > maxval:
                maxkey = key
                maxval = val
            elif val == maxval:
                maxkey = maxkey if maxkey > key else key

        return maxkey
