# @Time : 2022-08-10 17:27
# @Author : Phalange
# @File : 面试题 08.06. 汉诺塔问题.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)

        self.move(n,A,B,C)

    def move(self,n,A,B,C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n-1,A,C,B)
            C.append(A[-1])
            A.pop()
            self.move(n-1,B,A,C)

