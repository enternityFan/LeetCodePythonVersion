#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：main2.py
@Author ：HuntingGame

C'est la vie!!! enjoy ur day :D
'''

def f(x):
    return (1 + x) * x // 2

while True:
    try:
        l = list(map(int,input().strip().split()))
        if len(l) == 1:
            continue
        x,y = l[0],l[1]
        if x > y:
            x,y = y,x
        ans = y - x
        for i in range(2,y - x):
            # 尝试每种情况
            tmp = 0
            for j in range(i+1):
                # 1....k
                tmp +=j

            for j in range(i):
                #k-1...1
                tmp +=j
            #print("i= ",i,"tmp = ",tmp)
            if tmp > y - x:
                # 越界
                break
            unfinished = y - x - tmp
            ans = min(ans,2 * i + unfinished // i - int(unfinished % i == 0))
        print(ans)
    except EOFError:
        break