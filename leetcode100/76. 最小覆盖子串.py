#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：76. 最小覆盖子串.py
@Author ：HuntingGame
@Date ：2023-02-03 14:32 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        如果t的长度是M，s长度是N；如果M》N，那就不用讨论，是没的
        只有N>=M才可以；
        解题思路：做一个欠账表，是t的词频，那么遍历s，如果s[i]不在欠账表中，欠账表里面加个-1,但是欠账量不变；
        如果出现在，那就欠账表中i位置减一个，欠账量也减。直到欠账量变为0，那么这个时候L。。。R是一个符合的，不过不是最短的。
        这个时候L往右走，R往左缩，直到达标的最短。
        :param s:
        :param t:
        :return:
        """
        if len(s) <len(t):
            return ""
        map = [0] * 256
        for c in t:
            map[ord(c)] +=1
        L = 0
        R = 0
        match = len(t)
        minlen = -1
        ansl = -1
        ansr = -1
        # 窗口是左闭右开的，[L,R)
        while R !=len(s):
            map[ord(s[R])] -=1 #欠账减减
            if map[ord(s[R])]>=0:#有效还账
                match -=1
            if match == 0:
                #表示还完涨了
                while map[ord(s[L])] < 0:
                    #开始缩,判断能不能往右缩
                    #比如s:steasac,t:aac,这里就是在做把[L]从s到a的操作.
                    map[ord(s[L])]+=1
                    L +=1
                # 代码到这里，说明[L] == 0
                if minlen == -1 or minlen > R- L + 1:
                    #表示之前没有抓过答案或者之前答案没有现在的好。
                    minlen = R - L + 1
                    ansl = L
                    ansr = R
                match +=1#阴为上面的L，所以这里[L]一定是属于欠账表的。
                map[ord(s[L])] +=1#因为上面已经抓去过以L开头的最短距离了，现在L往右移一位来抓新的
                L +=1
            R +=1

        return s[ansl:ansr+1] if minlen !=-1 else ""







