# @Time : 2022-09-14 21:03
# @Author : Phalange
# @File : 845. 数组中的最长山脉.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        if n < 3:
            return 0
        tmp = 0
        flag = 0 #表示在左边，为1表示在右边
        for i in range(n):
            if (i!=n-1 and arr[i] < arr[i+1]) and flag==0:
                tmp +=1
            elif (i!=n-1 and arr[i] > arr[i+1]) and (flag==1 or (i!=0 and arr[i] > arr[i-1])):
                tmp +=1
                flag = 1
            else:
                if flag:
                    tmp = tmp + 1
                    flag = 0
                    ans = max(ans,tmp)
                tmp = 1 if i!=n-1 and arr[i] < arr[i+1] else 0

        return ans

arr = [875,884,239,731,723,685]
print(Solution().longestMountain(arr))