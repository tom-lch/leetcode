"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。

 

示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-perimeter-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # 方法繁琐
        if len(A)<3:
            return 0
        A.sort()
        if len(A)>=3:
            for i in range(len(A)-2):
                B = A[len(A)-3-i:len(A)-i]
                if B[0]>0 and B[0]+B[1]>B[2]:
                    return sum(B)
            return 0