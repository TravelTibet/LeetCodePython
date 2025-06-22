# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 22:12
# @File ：35Search_insertion_location.py
# @IDE ：PyCharm

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。

from typing import List


class Solution:
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


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 4))
