#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：K排序.py
@Author ：HuntingGame
@Date ：2023-03-26 17:03 
C'est la vie!!! enjoy ur day :D
在算法中，有各种各样的排序算法，例如归并排序，冒泡排序，快速排序等等。本题中，我们会使用种新的排序算法:K排序K排序算法描述如下:
首先，算法需要按照某种规则选择该数列上至多K个位置，将其对应的数抽出来，其他的数都往左对齐，之后这K个数排好序之后依次放在原数列末尾。以上过程算作一次操作。例如，对于数列[1,3,5,4,2]，当K=2时可以选择数字5和4，之后数列变成[1,3,2,4,5]。你的任务是:对于给定的数列，你需要计算出最少需要多少次上述操作，使得整个数列从小到大排好第一行一个正整数T，表示有T组数据。对于每一组数据，第一行输入两个正整数n,k; 第二行输入n个数a,az....a。该序列是一个1~n的排列对于所有数据:1sk<n<105,1<a:<n,afa1<T<5输出猫述
序?
[1,3,5,4,2]
[1,2,3,4,5]
'''
T = eval(input())
for _ in range(T):
    tmp = list(map(int, input().strip().split()))
    n,k = tmp[0],tmp[1]
    nums = list(map(int,input().strip().split()))
    ans = 0 #记录操作次数
    if n ==k:
        print(ans)
        continue
    for j in range(n):
        if nums[j] !=j+1:
            ans+=1
    if ans % k == 0:
        print(ans // k)
    else:
        print(ans // k+1)







