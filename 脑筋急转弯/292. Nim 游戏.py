#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：292. Nim 游戏.py
@Author ：HuntingGame
@Date ：2022/9/17 12:12 
C'est la vie!!! :)
'''


class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        你和你的朋友，两个人一起玩 Nim 游戏：
        桌子上有一堆石头。
        你们轮流进行自己的回合， 你作为先手 。
        每一回合，轮到的人拿掉 1 - 3 块石头。
        拿掉最后一块石头的人就是获胜者。
        1   1
        2   1
        3   1

        4   0
        5   1
        6   1
        7   1
        8   0
        9   1
        10  1
        11  1
        12  0

        """
        n = n % 4
        if n == 0:
            return False

        return True
