#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：小美刷怪.py
@Author ：HuntingGame

C'est la vie!!! enjoy ur day :D
小美在玩一项游戏。该游戏的目标是尽可能抓获敌人。
敌人的位置将被一个二维坐标(x,y)所描述。
小美有一个全屏技能，该技能能一次性将若干敌人一次性捕获。审获的敌人之间的横坐标的最大差值不能大于A，纵坐标的最大差值不能大于B。
现在给出所有敌人的坐标，你的任务是计算小美一次性最多能使用技能捕获多少敌人


'''

N, A, B = None, None, None
matrix = [[0 for _ in range(1001)] for i in range(1001)]
maxi,maxj = 0,0
mini,minj = 1001,1001
while True:
    try:

        l = list(map(int,input().strip().split()))
        if len(l) == 3:
            M,A,B=l[0],l[1],l[2]
            continue

        matrix[l[0]][l[1]] = 1 #表示有敌人
        #下面对矩阵进行优化，减少重复的计算
        maxi = max(maxi,l[0]+A)
        maxj = max(maxj,l[1]+B)
        mini = min(mini,l[0])
        minj = min(minj,l[1])


    except :
        maxans = -1

        # 预计算前缀和s[][]，也是n*m的矩阵
        s = [[0 for _ in range(1001)] for i in range(1001)]  # 初始化为n+1行m+1列的全0矩阵
        for i in range(1, maxi+1):
            for j in range(1, maxj+1):
                print(i,j)
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + matrix[i][j]

        # 四条边，每次移动一边，需要四个for循环遍历所有可能的矩阵
        for i1 in range(mini, maxi+1):  # 上边
            print("i1 = ",i1)
            for j1 in range(minj, maxj+1):  # 左边
                for i2 in range(i1,i1+A+1):  # 下边
                    if i2 > maxi+1:
                        break
                    for j2 in range(j1,j1+B+1):  # 右边
                        if j2 >maxj+1:
                            break

                        # 计算这个区域的总和
                        tmp = s[i2][j2] - s[i2][j1-1]-s[i1-1][j2] + s[i1-1][j1-1]
                        maxans = max(maxans,tmp)
        print(maxans)
        break
"""        
3 1 1
1 1
1 2
1 3

        
        
        """