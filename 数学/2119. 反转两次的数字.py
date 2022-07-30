# @Time : 2022-07-29 17:13
# @Author : Phalange
# @File : 2119. 反转两次的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num % 10 == 0 and num !=0:
            return False
        return True