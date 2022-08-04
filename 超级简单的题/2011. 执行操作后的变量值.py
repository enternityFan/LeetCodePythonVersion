# @Time : 2022-08-04 18:54
# @Author : Phalange
# @File : 2011. 执行操作后的变量值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for each in operations:
            if each == "--X" or each == "X--":
                X -=1
            elif each == "++X" or each == "X++":
                X +=1
        return X