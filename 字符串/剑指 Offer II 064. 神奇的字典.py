#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 19:07
# @Author  : HuntingGame
# @FileName: 剑指 Offer II 064. 神奇的字典.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            if len(word) not in self.dict:
                self.dict[len(word)] = []
            self.dict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.dict:
            return False
        for i in range(len(self.dict[len(searchWord)])):
            ans = 0

            for j in range(len(self.dict[len(searchWord)][i])):
                if self.dict[len(searchWord)][i][j] == searchWord[j]:
                    print(searchWord[j])
                    ans += 1

            if ans == len(searchWord) - 1:
                return True
        return False








# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello","leetcode"])
print(obj.search("hello"))