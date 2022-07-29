# @Time : 2022-07-29 20:10
# @Author : Phalange
# @File : 1534. 统计好三元组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        length = len(arr)
        count = 0
        for i in range(length):
            for j in range(i+1,length):
                if abs(arr[i] - arr[j]) <=a:

                    for k in range(j+1,length):

                        if abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <=c:
                            count +=1
        return count


s =Solution()
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(s.countGoodTriplets(arr,a,b,c))


