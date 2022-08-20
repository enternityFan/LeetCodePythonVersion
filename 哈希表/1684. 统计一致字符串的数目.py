# @Time : 2022-08-20 17:06
# @Author : Phalange
# @File : 1684. 统计一致字符串的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for each in words:
            flag = 0
            for c in set(each):
                if c not in allowed:
                    flag = 1

                    break

            if flag == 0:
                ans +=1
        return ans
