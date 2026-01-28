# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/25 10:00
# @File ：18_fourSum.py
# @IDE ：PyCharm
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
# （若两个四元组元素一一对应，则认为两个四元组重复）：
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
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


s = Solution()
print(s.fourSum([-13], 0))
