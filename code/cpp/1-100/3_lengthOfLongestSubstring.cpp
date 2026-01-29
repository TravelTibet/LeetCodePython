#include <bits/stdc++.h>

// 题目
// 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

//速度和空间占用依然很高
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> dict;
        int nStrLength = s.size(), i = 0, nMaxLength = 0, nNowLength = 0;
        while (i < nStrLength)
        {
            char c = s[i];
            auto [it, bIsInsert] = dict.try_emplace(c, i + 1);
            if (bIsInsert)
            {
                ++i;
                ++nNowLength;
            }
            else
            {
                i = it->second;//指针回退
                dict.clear();
                nMaxLength = max(nMaxLength, nNowLength);
                nNowLength = 0;
            }
           
        }
        return max(nMaxLength, nNowLength);
    }
};


int main(void)
{
    Solution S;
    int nRes = S.lengthOfLongestSubstring("adasd");
    cout << nRes;
	return 0;
}