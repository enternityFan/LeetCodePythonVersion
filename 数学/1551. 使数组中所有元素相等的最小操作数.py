# @Time : 2022-10-02 12:25
# @Author : Phalange
# @File : 1551. 使数组中所有元素相等的最小操作数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(0,n):
            arr.append(2*i+1)
        target = sum(arr) // n
        ans = 0
        for i in range(0,n //2):
            ans +=(target - arr[i] )

        return ans

