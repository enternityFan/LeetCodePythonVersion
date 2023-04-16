#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：小红书研究溶液.py
@Author ：HuntingGame
C'est la vie!!! enjoy ur day :D


实验室需要配制一种溶液。现在，研究员面前有n种该物质的溶液，每一种有无限多瓶，第i种的溶液体积为Xi，里面含有y;单位的该物质。研究员每次可以选择一瓶溶液，将其倒入另外一瓶(假设瓶子的容量无限)，即可以看作将两个瓶子内的溶液合并。此时合并的溶液体积和物质含量都等于之前两个瓶子内的之和。
特别地，如果瓶子A与B的溶液体积相同，那么A与B合并之后该物质的含量会产生化学反应，使得该物质含量增加X单位。
研究员的任务是配制溶液体积恰好等于C的，且尽量浓的溶液(即物质含量尽量多) 。研究员想要知道物质含量最多是多少。
输入描述
第一行三个正整数n,X,C;
第二行n个正整数X1X2..,n，中间用空格隔开
第三行n个正整数y1y2.yn，中间用空格隔开
对于所有数据，1<n,X,C,y;s1000,1<x;C
数据保证至少存在一种方案能够配制溶液体积恰好等于C的溶液。
输出描述
输出一行一个整数，表示答案。
样例输入
3416
5 3 4
24
样例输出
29

'''



def process(n,X,C,arrx,arry):
    if n == 1:
        return arry[0]
    dp = [[0 for _ in range(C+1)] for i in range(n)]
    # dp[i][j]表示只使用arrx[0...i]的溶液，凑出来的y的最大值
    #dp[i][0] = 0
    for j in range(1,C+1):
        if j % arrx[0] ==0:
            if dp[0][j//2] >0:
                dp[0][j] = 2*dp[0][j//2] + X
                continue
            tmp = (j // arrx[0]) #计算需要额外加多少X
            dp[0][j] = tmp* arry[0]
            dp[0][j] +=(tmp // 2) * X
        else:
            dp[0][j] = -1
    #普遍情况
    for i in range(1,n):
        for j in range(1,C+1):
            dp[i][j] = -1
            if dp[i-1][j] !=-1:
                # 说明只使用前面的就能凑出来
                dp[i][j] = dp[i-1][j]
            if j - arrx[i] >=0 and dp[i][j - arrx[i]] !=-1:
                tmp = dp[i][j-arrx[i]] + arry[i]
                if arrx[i] == j - arrx[i]:
                    tmp +=X
                dp[i][j] = max(dp[i][j],tmp)
    return dp[-1][-1]


# 这个题我觉得就是也给典型的零钱兑换的问题.
l = list(map(int,input().strip().split()))
n,X,C = l[0],l[1],l[2]
arrx = list(map(int,input().strip().split()))
arry = list(map(int,input().strip().split()))
arrx,arry = zip(*sorted(zip(arrx,arry)))#按照x进行排序



print(process(n,X,C,arrx,arry))

"""
3 4 16
5 3 4
2 4 1
"""