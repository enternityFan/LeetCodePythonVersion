# @Time : 2022-08-01 20:04
# @Author : Phalange
# @File : 67. 二进制求和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
