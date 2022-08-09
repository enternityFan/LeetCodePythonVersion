# @Time : 2022-08-09 18:37
# @Author : Phalange
# @File : LCS 02. 完成一半题目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        mycnt = collections.Counter(questions)
        mycnt = sorted(mycnt.items(),key=lambda x:x[1],reverse=True)
        n = len(questions) // 2
        ans = 0
        tmp = 0
        for each in mycnt:
            if tmp + each[1] < n:
                ans +=1
                tmp +=each[1]

            else:

                ans +=1
                break
        return ans
