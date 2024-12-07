# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:18
# @Author  : xiname
# @File    : 35.searchInsert.py
# @IDE     : PyCharm
from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    # 二分查找
    if target in nums:
        return nums.index(target)
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return low