# @Time : 2022-07-29 18:08
# @Author : Phalange
# @File : 357. 统计各位数字都不同的数字个数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        arr = [1,10,91]
        if n <=2:
            return arr[n]
        for i in range(3,n+1):
            arr.append( arr[i-1] + (arr[i-1]-arr[i-2]) * (10-(i-1)))

        return arr[n]
