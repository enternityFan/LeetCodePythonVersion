#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：22. 括号生成.py
@Author ：HuntingGame
@Date ：2023-02-02 9:08 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = ""
        self.process(path,0,0,n,ans)

    def process(self,path,index,leftNum,leftRest,ans):
        """
        path[0...index-1]的决定已经做完了，需要决定index位置上是(还是)
        如果还可以加左括号，那就加。如果还可以加右括号，那就加右。
        :param path:
        :param index:
        :param leftNum: 0到index-1区域左括号数量减去有括号数量的值
        :param leftRest: 还可以填多少个左括号
        :param ans:
        :return:
        """
        if index == len(path):
            ans.append(path)
        else:
            if leftRest > 0: #剪枝操作
                path += '('
                self.process(path,index+1,leftNum+1,leftRest-1,ans)

            if leftNum > 0:
                # 剪枝操作
                path +=')'
                self.process(path,index + 1,leftNum-1,leftRest,ans)
