# @Time : 2022-08-07 10:37
# @Author : Phalange
# @File : 6138. 最长理想子序列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
        这是一个动态规划的问题
        :param s:
        :param k:
        :return:
        """


        n = len(s)
        if n ==1:
            return s
        arr = [] # 用来维护一个你想子序列
        for c in s:
            pass

