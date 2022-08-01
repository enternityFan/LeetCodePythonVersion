# @Time : 2022-08-01 8:38
# @Author : Phalange
# @File : 1374. 生成每种字符都是奇数个的字符串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D





class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a" * (n-1) + "b"

        else:
            return "a"*n



