#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：小美字符串.py
@Author ：HuntingGame

C'est la vie!!! enjoy ur day :D
小美因为自己差劲的表达能力而苦恼，小美想制作一个解释器，这样她可以在无法表达的情况下让释器帮她解释。好巧不巧小美翻开了编译原理的书，找到了解释器的制作方式，她决定先制作一个
题目描述:
上习题中描述的小小解释器试试。小美需要读入一行字符串，其格式为"key1=val; key2=val2; ...; keyn-1=valn-1; keyn=valn;"(7含引号)这样的n对key,value对，其中key;和val;为第i对key,value对，且均为仅包含大小写英文字
母、数字与斜杠的非空字符串。例如对于字符串"SHELL=/bin/bash;HOME=/home/xiaomei;LOGNAME=xiaomei;"，那么其中包含三对key;value对，以(key;value)形式展示，分别为(SHELL,/bin/bash)、(HOME,/home/xiaomei).
(LOGNAMExiaomei)。接下来，小美的解释器需要接受q次询问，每次询问给出一个仅包含大小写英文字母、数字与斜杠非空字符串，如果存在某对key,value对的key值与之相同，那么输出对应的value; 如果存在多对key,value对的key值与之相同，那么输出其中编号最大的，也即最后那一对的value值;如果一对不存在，那么输出EMPTY。
'''
#LOGNAME=default;SHELL=/bin/bash;HOME=/home/xiaomei;LOGNAME=xiaomei;

s = input()
q = eval(input())
try:
    list_s = s.split(";")
except:
    list_s = []
mydict = {}
for each in list_s:
    if each == "":
        continue
    idx = each.find("=")
    if  idx !=-1:
        print(each[:idx],each[idx+1:])
        mydict[each[:idx]] = each[idx+1:] #这样就保证了序号大的覆盖掉前面的了

for _ in range(q):
    tmp = input()
    if tmp not in mydict:
        print("EMPTY")
        continue
    print(mydict[tmp])



