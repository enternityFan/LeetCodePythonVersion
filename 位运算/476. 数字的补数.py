# @Time : 2022-08-01 20:52
# @Author : Phalange
# @File : 476. 数字的补数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def findComplement(self, num: int) -> int:
        strnum = bin(num)[2:]
        strnum =strnum.replace('0','2')
        strnum = strnum.replace('1','0')
        strnum = strnum.replace('2','1')
        return int(strnum,2)


print(Solution().findComplement(2))