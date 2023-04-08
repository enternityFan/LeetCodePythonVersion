#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：子数组异或和等于乘积.py
@Author ：HuntingGame
@Date ：2023-03-26 21:38 
C'est la vie!!! enjoy ur day :D
'''
def count_sub(n,A):
    count = 0
    pro_dict = {}
    xor_dict = {}
    pro = 1
    xor_sum = 0
    for i in range(n):
        pro *=A[j]
        xor_sum ^= A[j]
        pro_dict[i] = pro
        xor_dict[i] = xor_sum
        for j in range(i,n):
            pro *= A[j]
            xor_sum ^= A[j]
            if pro == xor_sum:
                count += 1
    return count
if __name__ == '__main__':
    n = int(input())
    A = list(map(int,input().split()))
    result = count_sub(n,A)
    print(result)