# @Time : 2022-08-13 10:01
# @Author : Phalange
# @File : 22. 括号生成.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.tmp = []
    def generateParenthesis(self, n: int) -> List[str]:
        """
        首先暴力递归求解
        :param n:
        :return:
        """
        def dfs(left,right):
            if len(self.tmp) == 2*n:
                self.ans.append("".join(self.tmp[:]))
                return
            if left < n:
                self.tmp.append("(")
                dfs(left+1,right)
                self.tmp.pop()

            if right < left:
                self.tmp.append(")")
                dfs(left,right+1)
                self.tmp.pop()

        dfs(0,0)
        return self.ans











