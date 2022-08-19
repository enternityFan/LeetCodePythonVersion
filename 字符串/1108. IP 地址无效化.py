# @Time : 2022-08-19 10:23
# @Author : Phalange
# @File : 1108. IP 地址无效化.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")