#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 31. 栈的压入、弹出序列.py
@Author ：HuntingGame
@Date ：2023-03-15 20:30 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st,j = [],0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j+=1
        return len(st) == 0