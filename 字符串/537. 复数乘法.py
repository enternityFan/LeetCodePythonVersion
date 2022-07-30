# @Time : 2022-02-25 8:08
# @Author : Phalange
# @File : 537. 复数乘法.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_int = num1.replace('i','').split("+")
        num2_int = num2.replace('i','').split("+")
        num1_int = [int(each) for each in num1_int]
        num2_int = [int(each) for each in num2_int]
        # 开始做乘法
        num_res = [num1_int[0] * num2_int[0] - num1_int[1] * num2_int[1]  ,num1_int[0] * num2_int[1]+num1_int[1] * num2_int[0]]
        return f'{num_res[0]}+{num_res[1]}i'



s = Solution()
num1 = "1+1i"
num2 = "1+1i"
print(s.complexNumberMultiply(num1,num2))