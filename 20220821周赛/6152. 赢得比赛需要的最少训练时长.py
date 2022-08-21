# @Time : 2022-08-21 10:30
# @Author : Phalange
# @File : 6152. 赢得比赛需要的最少训练时长.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        sumenergy = sum(energy)
        if initialEnergy <=sumenergy:
            ans +=(sumenergy - initialEnergy+1)

        for i in range(len(experience)):
            if initialExperience <= experience[i]:
                ans +=(experience[i]-initialExperience+1)
                initialExperience+=(experience[i]-initialExperience+1)

            initialExperience+=experience[i]
        return ans

initialEnergy = 2
initialExperience = 2
energy = [1]
experience = [1]
print(Solution().minNumberOfHours(initialEnergy,initialExperience,energy,experience))