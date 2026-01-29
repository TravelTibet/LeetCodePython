#include <bits/stdc++.h>
using namespace std;

// 题目
// 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

//速度和空间占用依然很高，法一用map，传统思想，需要回退比较慢
//class Solution {
//public:
//    int lengthOfLongestSubstring(string s) {
//        unordered_map<char,int> dict;
//        int nStrLength = s.size(), i = 0, nMaxLength = 0, nNowLength = 0;
//        while (i < nStrLength)
//        {
//            char c = s[i];
//            auto [it, bIsInsert] = dict.try_emplace(c, i + 1);
//            if (bIsInsert)
//            {
//                ++i;
//                ++nNowLength;
//            }
//            else
//            {
//                i = it->second;//指针回退
//                dict.clear();
//                nMaxLength = max(nMaxLength, nNowLength);
//                nNowLength = 0;
//            }
//           
//        }
//        return max(nMaxLength, nNowLength);
//    }
//};

//法二新思想，滑动窗口
class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
       int nStrSize = s.size();
        if (nStrSize == 0) return 0;
        unordered_set<char> set;
        int nMaxLength = 0;
        int nLeft = 0;
        char c = '0';
        for (int i = 0; i < nStrSize; ++i)
        {
            c = s[i];
            while (set.find(c) != set.end())
            {
                set.erase(s[nLeft]);
                ++nLeft;
            }
            set.emplace(c);
            nMaxLength = max(nMaxLength, i - nLeft + 1);
        }
        return nMaxLength;
    }
};

int main(void)
{
    Solution S;
    //int nRes = S.lengthOfLongestSubstring("abcabcwe");
    int nRes = S.lengthOfLongestSubstring("pwwkew");
    cout << nRes;
	return 0;
}