# @Time : 2022-08-20 17:14
# @Author : Phalange
# @File : 1832. 判断句子是否为全字母句.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26