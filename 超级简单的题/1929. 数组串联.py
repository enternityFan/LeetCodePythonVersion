# @Time : 2022-08-04 18:52
# @Author : Phalange
# @File : 1929. 数组串联.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums= nums + nums
        return nums