#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 58 - I. 翻转单词顺序.py
@Author ：HuntingGame
@Date ：2023-03-07 13:31 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = []
        blankIdx = -2#上一次出现空格的位置,-2表示首空格，-1表示中间的。

        for i in range(len(s)):
            if s[i] == " ":
                if blankIdx == -1:
                    blankIdx = i

            else:
                if blankIdx !=-1:
                    if blankIdx !=-2:
                        s2.append(s[blankIdx])
                    blankIdx = -1
                s2.append(s[i])
        #此时关于空格的问题全部处理好了，然后交换
        L = 0
        R = len(s2)-1
        while L <=R:
            s2[L],s2[R] = s2[R],s2[L]
            L +=1
            R -=1
        print(s2)
        s3 = ""
        word = ""
        for i in range(len(s2)):
            if s2[i] == " ":
                s3 +=word[::-1] + " "
                word = ""
            else:
                word +=s2[i]
        s3 +=word[::-1]
        return s3



s = "  hello   world!  "
print(Solution().reverseWords(s))