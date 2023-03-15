#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：946. 验证栈序列.py
@Author ：HuntingGame
@Date ：2023-03-15 20:33 
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
                j +=1
        return len(st ) == 0