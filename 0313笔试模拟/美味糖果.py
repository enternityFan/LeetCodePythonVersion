#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：美味糖果.py
@Author ：HuntingGame
小美特别爱吃糖果。小美家楼下正好有一个糖果专卖店，每天供应不同种类的糖果。小美预先拿糖果专卖店接下来n天的进货计划表，并针对每天的糖果种类标注好了对小美而言的美味值。小然想每天都能去买糖果吃，不过由于零花钱限制(小美零花钱并不多!)以及健康考虑，小美沙则上如果今天吃了，那么明天就不能吃。但小美认为凡事都有例外，所以她给了自己k次机会，天已经吃了糖果的情况下，今天仍然连续吃糖果!简单来说，小美每天只能吃一次糖果，原则上昨天吃了糖果那么今天就不能吃，但有最多k次机会打破这一原则。
小美不想浪费每次吃糖果的机会，所以请你帮帮她规划一下她的吃糖果计划，使得她能吃到的糊味值最大。
C'est la vie!!! enjoy ur day :D
'''
n,k = None,None
nums = None
while True:
    try:
        l = list(map(int,input().strip().split()))
        if len(l) == 2:
            n,k = l[0],l[1]
            #print(n,k)
            continue
        else:
            nums = l



    except EOFError:
        break
# n,k = None,None
# nums = None
# while True:
#     try:
#         l = list(map(int,input().strip().split()))
#         if len(l) == 2:
#             n,k = l[0],l[1]
#             #print(n,k)
#             continue
#         else:
#             nums = l
#         #max(奇数序列和，偶数序列和) + min(奇数序列和，偶数序列和）的前k大
#         odd = []
#         even = []
#         ans = 0
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 even.append(nums[i])
#             else:
#                 odd.append(nums[i])
#         flag = 0 #0表示偶数找k个，为1表示奇数序列找k个
#         if sum(even) > sum(odd):
#             ans +=sum(even)
#             flag = 1
#         else:
#             ans +=sum(odd)
#             flag = 0
#         if k >= len(odd):
#             print(sum(nums))
#             break
#         if flag:
#             odd.sort(reverse=True)
#             print(ans,ans + sum(odd[:k]))
#         else:
#             even.sort(reverse=True)
#             print(ans + sum(even[:k]))
#     except EOFError:
#         break
#1 2 3 4 5 6 7