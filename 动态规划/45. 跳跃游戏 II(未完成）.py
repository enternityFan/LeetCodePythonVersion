# @Time : 2022-08-13 10:16
# @Author : Phalange
# @File : 45. 跳跃游戏 II(未完成）.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         """
#         用递归去做，很明显，我需要知道当前的位置，有一个当前跳跃的次数
#         这个代码已经验证了，可以，不过超时。需要改为动态规划
#         :param nums:
#         :return:
#         """
#         ans = []#存放路径
#         tmp = [0]#存放路径
#
#         def process(idx,time):
#             if idx >= len(nums)-1:
#                 # 那么我就跳出去了已经
#                 ans.append(tmp[:])
#                 print(tmp)
#                 #tmp.pop()
#                 return time#表明成功
#
#             # 不然的话，我要一个个的去试
#             if nums[idx] ==0:
#                 #那就不说了，就没法跳了，是吧
#                 return 1e6 # 表示没法跳了
#             minTime = 1e6
#             for i in range(idx+1,idx+nums[idx]+1):
#                 #idx+nums[idx]是在当前位置，最远可以跳跃到的地方
#                 tmp.append(i)
#                 newTime = process(i,time+1)
#                 tmp.pop()
#                 #print(newTime)
#                 minTime = min(newTime,minTime)
#
#             return minTime
#
#
#
#
#             #ans.append(max(newIdx))
#             #process(max(newIdx))
#         times = process(0,0)
#         return times


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        把递归改为记忆化搜索，可以看出来，动态变化的参数，只有一个，并且，也只有这个影响结果，就是当前的位置idx

        :param nums:
        :return:
        """
        ans = []#存放路径
        tmp = [0]#存放路径
        dp = [0] * (len(nums)+1)
        def process(idx,time):#需要传入一个最原始的idx，就是这个账要记到谁头上
            if idx >= len(nums)-1:
                # 那么我就跳出去了已经
                ans.append(tmp[:])
                #print(tmp)
                #tmp.pop()
                dp[-1] = time # 更新一下？
                return time#表明成功
            # 不然的话，我要一个个的去试
            if nums[idx] ==0:
                #那就不说了，就没法跳了，是吧
                dp[idx] = 1e6
                return 1e6 # 表示没法跳了
            minTime = 1e6
            for i in range(idx+nums[idx]+1 if idx+nums[idx]+1 <len(nums) else len(nums)-1,idx,-1):
                #idx+nums[idx]是在当前位置，最远可以跳跃到的地方
                if dp[i] == 0:
                    tmp.append(i)
                    newTime = process(i,time+1)

                    tmp.pop()
                    #print(newTime)
                else:
                    print("here")
                    newTime = dp[i]
                minTime = min(newTime,minTime)
                dp[i] = minTime
            print(dp)
            return minTime




            #ans.append(max(newIdx))
            #process(max(newIdx))
        times = process(0,0)
        return times









print(Solution().jump([2,1]))

print(Solution().jump([2,3,0,1,4]))