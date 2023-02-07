#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：171. Excel 表列序号.py
@Author ：HuntingGame
@Date ：2023-02-07 20:14 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        注意这个不是26进制，老左说这是伪进制
        emmm这么说是因为他给每个数位的分配值的方式，看代码吧，一看就懂了。
        :param columnTitle:
        :return:
        """
        ans = 0
        for i in range(len(columnTitle)):
            ans = ans * 26 + (ord(columnTitle[i]) - ord('A')) + 1

        return ans






