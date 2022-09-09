# @Time : 2022-09-09 12:14
# @Author : Phalange
# @File : 1598. 文件夹操作日志搜集器.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for each in logs:
            if each == "./":
                continue
            elif each == "../":
                ans =ans -1 if ans !=0 else 0
            else:
                ans +=1

        return ans
