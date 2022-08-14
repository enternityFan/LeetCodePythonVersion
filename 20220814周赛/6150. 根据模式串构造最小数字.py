# @Time : 2022-08-14 10:46
# @Author : Phalange
# @File : 6150. 根据模式串构造最小数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# class Solution:
#     def smallestNumber(self, pattern: str) -> str:
#         ans = []# 记录所有的答案
#
#         def process(idx,tmp):
#             if idx == len(pattern):
#                 ans.append("".join(tmp))
#                 return
#
#             for i in range(len(tmp)):
#                 # 这个题，感觉有点像那个，八皇后
#                 if (pattern[idx] == "D" and tmp[idx] < tmp[idx+1]) or (pattern[idx] == "I" and tmp[idx] > tmp[idx+1]):
#                     tmp[i],tmp[i+1] = tmp[i+1],tmp[i]#交换一下位置
#
#                     tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]  # 交换一下位置
#
#                 process(idx+1)
#
#
#
#         tmp = list(range(1,len(pattern)+2))
#         process(0,tmp)
#         #找到最小字典序的一个操作


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        tmp = [str(i) for i in range(1,len(pattern)+2)]
        n = len(pattern)
        idxD = -1 #记录上一个出现D的
        for i in range(n):

            if pattern[i] == "D" and tmp[i] < tmp[i+1]:
                if idxD == -1:
                    idxD = i
                record = tmp[i+1]
                for j in range(i,idxD-1,-1):
                    tmp[j+1] = tmp[j]
                tmp[idxD] = record
            elif pattern[i] == "I" and idxD !=-1:
                idxD = -1

        return "".join(tmp)

print(Solution().smallestNumber("IIIDIDDD"))
