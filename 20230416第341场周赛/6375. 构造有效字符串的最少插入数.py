#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6375. 构造有效字符串的最少插入数.py
@Author ：HuntingGame
@Date ：2023-04-16 10:37 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        if len(word) == 1:
            return 2
        if len(word) == 2:
            if (word == "ab") or (word == "bc") or (word == "ac"):
                return 1
            else:
                return 4
        tmp = ""
        i = 0
        flag = 0
        while i < len(word)-2:
            if word[i:i+3] == "abc":
                if i+3 >=len(word):
                    flag = 1
                i +=3
                continue
            elif ((word[i:i+2] == "ab" ) or(word[i:i+2] == "bc") or (word[i:i+2] == "ac")):
                i+=2
                ans+=1
            else:
                i+=1
                ans +=2
        print(i)
        if flag == 0:
            if i == len(word)-2:
                if (word[-2:] == "ab") or (word[-2:] == "bc") or (word[-2:] == "ac"):
                    ans +=1
                else:
                    ans +=4
            else:
                ans +=2
        return ans

print(Solution().addMinimum("aaabca"))
