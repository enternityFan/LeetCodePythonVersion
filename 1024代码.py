#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1024代码.py
@Author ：HuntingGame
@Date ：2022-10-24 10:34 
C'est la vie!!! enjoy ur day :D
'''

from itertools import permutations


def getNum(candi_nums, candi_ops):
    res = candi_nums[0]
    for i in range(3):
        res = eval('(' + str(res) + ')' + candi_ops[i] + '(' + str(candi_nums[i + 1]) + ')')

    if res == 1024:
        print(candi_nums, candi_ops)


def get1024(nums, ops):
    candi_nums = list(permutations(nums, 4))
    candi_ops = list(permutations(ops, 3))

    for n in candi_nums:
        for o in candi_ops:
            getNum(n, o)


numbers = [ 2,2,2,2,4,8,2,2, 996,14,18,10,23,18,1,34,6, 33]
operators = ['%',  '-','^', '//']

#(((2&2)>>0)<<9)
ok = []

for n1 in range(len(numbers)):
    for n2 in range(len(numbers)):
        for n3 in range(len(numbers)):
            for n4 in range(len(numbers)):
                for o1 in range(len(operators)):
                    for o2 in range(len(operators)):
                        for o3 in range(len(operators)):
                            if (n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4) or (o1 == o2 or o2 == o3 or o1 == o3):
                                continue
                            string = f"((({numbers[n1]}{operators[o1]}{numbers[n2]}){operators[o2]}{numbers[n3]}){operators[o3]}{numbers[n4]})"
                            try:
                                if eval(string) == 1024:
                                    ok.append(string)
                                    print(string)
                            except:
                                continue

print(ok)
# (((2&2)-6)%9)