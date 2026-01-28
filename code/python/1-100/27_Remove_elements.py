# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/15 22:08
# @File ：27_Remove_elements.py
# @IDE ：PyCharm
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
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
                print('1:',high_point, low_point)
                # 两个指针的值不一样！
                low_point = i
                while low_point < len(nums):
                    temp = nums[low_point]
                    nums[low_point] = nums[high_point]
                    nums[high_point] = temp
                    high_point += 1
                    low_point += 1
                    print('2:',high_point, low_point)
                break
            else:
                high_point = len(nums)
        return high_point


s = Solution()
print(s.removeElement(nums=[2,6], val=3))
