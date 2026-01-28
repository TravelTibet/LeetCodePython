# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/25 9:22
# @File ：119_YangHuiTriangleTwo.py
# @IDE ：PyCharm
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        new_list = []
        # 其他情况：
        for numrow in range(0, rowIndex + 1):  # 题目最多是33行
            # 特例
            if numrow == 0:
                new_list.append([1])
                continue
            elif numrow == 1:
                new_list.append([1, 1])
                continue
            else:
                temp_list = [1]  # 每行第一个数都是1
                # 每一行应该有 n=numrow + 1 个数,这里 n 从 0 开始
                for num in range(1, numrow): # 只循环n - 2次，首尾都是1，额外处理
                    old_list = new_list[numrow - 1]  # 上一层的数组
                    temp_list.append(old_list[num - 1] + old_list[num])

                temp_list.append(1)  # 添加最后一个元素
                new_list.append(temp_list)

        return new_list[rowIndex]


s = Solution()
print(s.getRow(50))
