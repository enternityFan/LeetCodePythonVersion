# @Time : 2022-03-03 16:20
# @Author : Phalange
# @File : 最强战力兵团.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

import numpy as np


class Solution:
    def func(self,n,m,k,troops):
        # 初始化最强兵团
        troops = np.array(troops)
        maxScoreTroop = np.sum(np.array(troops[:k,:k]))

        for i in range(n-k+1):
            for j in range(m - k+1):
                # 开始滑动
                maxScoreTroop = max(maxScoreTroop,np.sum(np.array(troops[i:k+i,j:k+j])))

        return maxScoreTroop



s = Solution()

str = input().split(" ")

n,m,k = int(str[0]),int(str[1]),int(str[2])
a = []
for _ in range(n):
    b = []
    str = input().split(' ')
    for i in range(m):
        b.append(int(str[i]))
    a.append(b)
print(s.func(n,m,k,a))

#n,m = 4,4
#a = np.random.randint(1,50,[4,4])
#print(a)
#a = np.array([[1,2,3,4],[5,6,7,8],[7,6,5,4],[4,3,2,1]])
#print(s.func(n,m,2,a))