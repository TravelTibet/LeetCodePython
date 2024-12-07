# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:25
# @Author  : xiname
# @File    : 16.threeSumClosest.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        temp = inf
        for k in range(len(nums)):
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == target:
                    return s
                # 更新值
                if abs(s - target) <= abs(temp - target):
                    # print('s,k,i,j', s, nums[k], nums[i], nums[j])
                    temp = s
                # 移动指针
                if s <= target:
                    i += 1
                elif s > target:
                    j -= 1

        return temp
