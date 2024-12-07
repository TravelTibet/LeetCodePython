# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:24
# @Author  : xiname
# @File    : 15.threeSum.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 对数组排序
        nums.sort()
        new_nums = []
        # 特例
        if len(nums) < 3 or nums is None:
            return []
        for k in range(len(nums) - 1):
            # 结束条件
            if nums[k] > 0:
                break
            i, j = k + 1, len(nums) - 1
            while True:
                if i == j:
                    break
                sum_nums = nums[k] + nums[i] + nums[j]
                if sum_nums == 0:
                    temp_nums = [nums[k], nums[i], nums[j]]  # 注意顺序，用来判断是否重复的解
                    # print("k,i,j,temp_nums:",k,i,j,temp_nums)
                    if temp_nums not in new_nums:
                        new_nums.append(temp_nums)
                    i += 1
                # 移动指针
                elif sum_nums > 0:
                    j -= 1
                elif sum_nums < 0:
                    i += 1
        return list(new_nums)