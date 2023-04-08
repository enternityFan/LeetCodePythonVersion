#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：与或等.py
@Author ：HuntingGame
@Date ：2023-03-26 16:47 
C'est la vie!!! enjoy ur day :D
给出一个数组。你需要求出按顺序对其进行一系列区间操作后最终所得的数组。操作有三种:1.将下标在L到R之间的元素全部或上X。2将下标在L到R之间的元素全部与上X。3.将下标在L到R之间的元素全部设为X
'''

# 构建线段树
class BinaryIndexTree:

    def __init__(self, array: list):
        '''初始化，总时间 O(n)'''
        self._array = [0] + array
        n = len(array)
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                self._array[j] += self._array[i]

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, val: int):
        '''将原数组idx下标更新为val, 总时间O(log n)'''
        prev = self.query(idx, idx + 1)  # 计算出原来的值
        idx += 1
        val -= prev  # val 是要增加的值
        while idx < len(self._array):
            self._array[idx] += val
            idx += self.lowbit(idx)

    def query(self, begin: int, end: int) -> int:
        '''返回数组[begin, end) 的和'''
        return self._query(end) - self._query(begin)

    def _query(self, idx: int) -> int:
        '''计算数组[0, idx)的元素之和'''
        res = 0
        while idx > 0:
            res += self._array[idx]
            idx -= self.lowbit(idx)
        return res







# 读取输入数据
N = int(input()) # 数组长度
arr = list(map(int, input().split())) # 数组元素
M = int(input()) # 操作次数
L = list(map(int, input().split())) # 区间左端点
R = list(map(int, input().split())) # 区间右端点
op = input() # 操作类型
X = list(map(int, input().split())) # 操作参数
bit = BinaryIndexTree([0] * N)
for i in range(M-1,-1,-1):
    # 获取当前操作的信息
    l = L[i] - 1 # 下标从0开始
    r = R[i] - 1
    x = X[i]
    o = op[i]


    if o == "=": # 按位或运算
        for j in range(l, r + 1):
            arr[j] = x
            print(j+1)
            bit.update(j+1,1)#表示有了=的操作，j+1因为线段树从1开始的

    elif bit.query(l,r+1)== r+1-l:
        continue#不必操作！
    elif o == "&" : # 按位与运算
        for j in range(l, r + 1):
            arr[j] &= x
    elif o == "|": # 赋值运算
        for j in range(l, r + 1):
            arr[j] |= x
print(*arr)

"""
4
5 4 7 4
4
1 2 3 2
4 3 4 2
=|&=
8 3 6 2

"""