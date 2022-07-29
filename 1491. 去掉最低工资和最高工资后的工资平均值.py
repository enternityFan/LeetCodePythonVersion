# @Time : 2022-07-29 11:21
# @Author : Phalange
# @File : 1491. 去掉最低工资和最高工资后的工资平均值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary)-2)