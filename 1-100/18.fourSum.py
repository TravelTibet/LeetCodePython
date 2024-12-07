# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:25
# @Author  : xiname
# @File    : 18.fourSum.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 预处理、排序
        nums.sort()
        new_nums = []
        for m in range(len(nums)):
            for k in range(len(nums)):
                # n 从末尾开始
                n = len(nums) - k - 1
                i, j = m + 1, n - 1
                while i < j:
                    s = nums[m] + nums[i] + nums[j] + nums[n]  # 注意顺序，用来判断是否重复
                    if s < target:
                        i += 1
                    elif s > target:
                        j -= 1
                    elif s == target:
                        temp_nums = [nums[m], nums[i], nums[j], nums[n]]  # 注意顺序
                        if temp_nums not in new_nums:
                            new_nums.append(temp_nums)
                        j -= 1

        return new_nums