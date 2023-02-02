#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：33. 搜索旋转排序数组.py
@Author ：HuntingGame
@Date ：2023-02-02 11:23 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        这个题考条件分类。最坏情况是O(N)的，他考你能二分你就二分。 :param nums:
        :param target:
        :return:
        """
        L = 0
        R = len(nums) -1
        M = 0
        while L <=R: #注意有等号
            M = (L + R) / 2
            if nums[M] == target:
                return M

            if nums[L] == nums[M] and nums[M] == nums[R]:
                # 这种情况是没法二分的，要调整L的值。比如说Nums=222222222212222,这个找1是根本没法二分的，谁知道这个1在哪
                #如果L移动到M也是2，那就在M+1到R位置二分嘛。最坏的情况是O(N)的所以是。
                while L !=M and nums[L] == nums[M]:
                    L +=1

                if L == M:
                    L = M + 1
                    continue



            #[L] [M] [R]不都一样
            if nums[L] !=nums[M]:
                if nums[M] > nums[L]:
                    # 这就说明M之前是有序的。
                    if target >= nums[L] and target < nums[M]:
                        R = M - 1
                    else:
                        L = M +1
                else:
                    # 到这里的话，说明[L] > [M],那么肯定知道M之后是有序的，如果target在[M],[R]的范围，那就在这里面找就行了。
                    if target >nums[M] and target <= nums[R]:
                        L = M + 1
                    else:
                        R = M - 1
            else:
                # 这里隐含了[M] !=[R]

                if nums[M] < nums[R]:
                    # 这就说明M之后是有序的。
                    if target > nums[M] and target <= nums[R]:
                        L = M +1
                    else:
                        R = M - 1
                else:
                    # 到这里的话，说明[L] > [M],那么肯定知道M之后是有序的，如果target在[M],[R]的范围，那就在这里面找就行了。
                    if target > nums[L] and target <= nums[M]:
                        R = M - 1
                    else:
                        L = M + 1
        return -1
