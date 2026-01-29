"""
@Project ：LeetCode
@File    ：3_lengthOfLongestSubstring.py
@IDE     ：PyCharm 
@Author  ：XiName
@Date    ：2026/1/28 09:46 
"""


# 题目
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

# 采用内置字典的办法，时间和空间消耗在提交排名中靠后...
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempDict = dict()
        maxLen = 0
        nowLen = 0

        index = 0
        strLength = len(s)
        while index < strLength:
            char = s[index]
            if char in tempDict:
                index = tempDict.get(char)  # 回退
                tempDict.clear()
                maxLen = max(maxLen, nowLen)
                nowLen = 0

            else:
                tempDict[char] = index + 1
                nowLen += 1
                index += 1
        return max(maxLen, nowLen)


if __name__ == '__main__':
    S = Solution()
    result = S.lengthOfLongestSubstring("abac")
    # result = S.lengthOfLongestSubstring("pwwkew")
    print(f"Length of longest substring: {result}")
