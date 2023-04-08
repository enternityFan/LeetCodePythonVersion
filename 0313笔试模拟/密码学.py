#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：密码学.py
@Author ：HuntingGame
@Date ：2023-03-26 16:36 
C'est la vie!!! enjoy ur day :D
小明学会了一种加密方式。他定义suc(x)为x在字母表中的后继，例如a的后继为b，b的后继为c...(即按字母表的顺序后一个)。特别的，z的后继为a。对于一个原字符串S，将其中每个字母x都替换成其三重后继，即suc(suc(suc(x)))的字母，即完成了加密。例如，abc加密后变成def (suc(suc(suc(a))=d suc(suc(suc(b))=e suc(suc(suc(c)))=f)
现在小明知道一个加密后的字符串S，想请你找出他的原串S
'''

mydict = {}
tmp = "a"
for i in range(3,26):
    mydict[chr(ord(tmp) + i)] = chr(ord(tmp) + i-3)
#print(mydict)
mydict['a'] = 'x'
mydict['b'] = 'y'
mydict['c'] = 'z'

N = eval(input())

s = input()
ans = ""
for c in s:
    ans +=mydict[c]
print(ans)
