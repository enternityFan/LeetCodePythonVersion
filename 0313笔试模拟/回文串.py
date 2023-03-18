#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：回文串.py
@Author ：HuntingGame
@Date ：2023-03-18 11:32 
C'est la vie!!! enjoy ur day :D



现在小美获得了一个字符串。小美想要使得这个字符串是回文串小美找到了你。你可以将字符串中至多两个位置改为任意小写英文字符’a’-z你的任务是帮助小美在当前制约下，
获得字典序最小的回文字符串。数据保证能在题目限制下形成回文字符串。
注:回文字符串:即一个字符串从前向后和从后向前是完全一致的字符串。例如字符串abcba,aaaa,acca都是回文字符串。字符串abcd,acea都不是回文字符次
'''

s = input()
midlen = len(s) // 2 #找到中间的位置
cnts1 = [0] * 26 #前半段的频次
cnts2 = [0] * 16 #后半段的频次
first = [-1] * 16 #最早出现的位置
for i in range(len(s)):
    if i == midlen and len(s):
        pass














