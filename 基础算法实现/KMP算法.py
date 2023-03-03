#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：KMP算法.py
@Author ：HuntingGame
@Date ：2023-02-27 20:23 
C'est la vie!!! enjoy ur day :D
'''



"""
实现KMP算法
"""


def myKMP(text,match):

    i = 0#指向text的指针
    j = 0# 指向match的指针
    nexts = get_next(match)
    while i < len(text) and j < len(match):
        if text[i] == match[j]:
            i+=1
            j+=1
        elif nexts[j] == -1:
            # 说明j = 0
            i+=1
        else:
            j = nexts[j]

    return i - j if j == len(match) else -1




def get_next(match):
    """
    得到next数组
    :param match:
    :return:
    """
    if len(match) == 1:
        return -1

    nexts = [0] * len(match)
    nexts[0] = -1
    nexts[1] = 0
    i = 2
    cn = 0# 当前和i-1位置比较的字符
    while i < len(nexts):
        if match[i-1] == match[cn]:
            nexts[i] = cn + 1
            i +=1
            cn+=1
        elif cn > 0:
            cn = nexts[cn]
        else:
            nexts[i] = 0
            i +=1
    return nexts









if __name__ == "__main__":
    text = "hello world!ababacd"
    match = "ab"
    print(myKMP(text,match))


