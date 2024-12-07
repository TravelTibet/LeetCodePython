# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:17
# @Author  : xiname
# @File    : 27.removeElement.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        # 传入数组空的时候，直接返回0
        high_point = 0
        low_point = 0
        for i in range(len(nums)):
            if nums[i] == val:
                # 先找到第一个不一样的值
                high_point = i
                low_point = i
                while i < len(nums) and nums[i] == val:
                    i += 1
                print('1:', high_point, low_point)
                # 两个指针的值不一样！
                low_point = i
                while low_point < len(nums):
                    temp = nums[low_point]
                    nums[low_point] = nums[high_point]
                    nums[high_point] = temp
                    high_point += 1
                    low_point += 1
                    print('2:', high_point, low_point)
                break
            else:
                high_point = len(nums)
        return high_point
