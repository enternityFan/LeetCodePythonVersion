#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/21 13:50
# @Author  : HuntingGame
# @FileName: NC127 最长公共子串.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D



#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        if not str1 or not str2 or str1 == "" or str2 == "":
            return ""
        row = 0
        col = len(str1) - 1
        ans = 0
        end = 0
        while row < len(str1):
            i = row
            j = col
            tmp = 0
            while i < len(str1) and j < len(str2):
                if str1[i] == str2[j]:
                    tmp +=1
                else:
                    tmp = 0

                if tmp > ans:
                    end = i
                    ans = tmp
                i+=1
                j+=1

            if col >0:
                col -=1
            else:
                row +=1

        return str1[end-ans+1:end+1]












