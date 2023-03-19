#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6323. 将钱分给最多的儿童.py
@Author ：HuntingGame
@Date ：2023-03-18 22:30 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money // children == 8 and money % children == 0:
            return children
        if money <children:
            return -1
        elif money == children:
            return 0

        ans = 0
        i = 0
        while i < children and money >0:
            if money == 12 and children -i == 2:
                money = 0
                i = children
                break
            if money - 8 >=0 and (money - 8) >= children-i-1:
                money -=8
                ans +=1
                i +=1
            elif 8 >= money >= children - i:
                i = children
                money = 0
                break

            else:
                i = children
                money = 0
                break


        if i !=children:
            return -1
        if money:
            ans -=1
        return ans

print(Solution().distMoney(17,5))





