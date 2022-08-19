# @Time : 2022-08-19 14:21
# @Author : Phalange
# @File : 2108. 找出数组中的第一个回文字符串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for each in words:

            flag = 0

            for i in range(len(each)//2):
                if each[i] != each[len(each)-1-i]:
                    flag = 1
                    break

            if flag == 0:
                ans = each
                break


        return ans