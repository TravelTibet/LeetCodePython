#include <bits/stdc++.h>
using namespace std;
//题目
//给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是(i, 0) 和(i, height[i]) 。
//找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
//返回容器可以储存的最大水量。

class Solution {
public:
    int maxArea(vector<int>& height) {
        int nLeft = 0, nRight = height.size() - 1;
        int nMaxArea = 0;
        while (nLeft != nRight)
        {
            nMaxArea = max(nMaxArea, min(height[nLeft], height[nRight]) * (nRight - nLeft));
            if (height[nLeft] < height[nRight])
            {
                ++nLeft;
            }
            else
            {
                --nRight;
            }
        }
        nMaxArea = max(nMaxArea, min(height[nLeft], height[nRight]) * (nRight - nLeft));
        return nMaxArea;
    }
};

//int main()
//{
//    Solution S;
//    //vector<int> height = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
//    vector<int> height = { 1,1 ,1};
//    cout << S.maxArea(height);
//	return 0;
//}