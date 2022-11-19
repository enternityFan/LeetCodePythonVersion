#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：819. 最常见的单词.py
@Author ：HuntingGame
@Date ：2022-11-14 11:00 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        mydict = collections.defaultdict(int)

        word = ""
        paragraph = paragraph.lower()
        for i in range(len(paragraph)):
            if paragraph[i] in "!?' ,;.":
                mydict[word] +=1
                word = ""
            else:
                word +=paragraph[i]

        if word != "":
            mydict[word] +=1
        maxlen,ans = 0,""
        for key,val in mydict.items():
            if key not in banned:
                if val > maxlen:
                    maxlen = val
                    ans = key
        return ans
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
print(Solution().mostCommonWord(paragraph,['hit']))