# @Time : 2022-08-20 8:11
# @Author : Phalange
# @File : 1395. 统计作战单位数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.ai = [0] * 1001
        self.aj = [0] * 1001
        self.ak = [0] * 1001
        #self.mymap = {}#里面的值是存放的这个东西，key是i+j+k的值，val是对应的[]
    def numTeams(self, rating: List[int]) -> int:

        self.process2(rating,0,1,2)
        return self.ans



    def process2(self,nums,i,j,k):
        if i < j < k and k < len(nums):
            if (nums[i] < nums[j] and nums[j] < nums[k]) or (nums[i] > nums[j] and nums[j] > nums[k]):
                tmp = [nums[i],nums[j],nums[k]]
                self.ai[i] = 1
                self.aj[j] = 1
                self.ak[k] = 1
                self.ans.append(tmp)



            self.process2(nums,i,j,k+1)
            if self.ai[i]+self.aj[j+1]+self.ak[k+1]!=3:
                self.process2(nums,i,j+1,k+1)
            if self.ai[i+1]+self.aj[j+1]+self.ak[k+1]!=3:
                self.process2(nums,i+1,j+1,k+1)


        else:

            return # 不然的话就不行的。






    def process3(self,nums,i,j,k):
        """
        i < j < k,且rating[i] < rating[j] < rating[k],或者是rating[i] > rating[j] > rating[k]
        :param i:
        :param j:
        :param k:
        :return:
        """
        if i < j < k and k < len(nums):
            if (nums[i] < nums[j] and nums[j] < nums[k]) or (nums[i] > nums[j] and nums[j] > nums[k]):
                tmp = [nums[i],nums[j],nums[k]]
                if tmp not in self.ans:
                    self.ans.append(tmp)

            self.process3(nums,i,j,k+1)
            self.process3(nums,i,j+1,k+1)
            self.process3(nums,i+1,j+1,k+1)


        else:

            return # 不然的话就不行的。


print(Solution().numTeams([4,7,9,5,10,8,2,1,6]))