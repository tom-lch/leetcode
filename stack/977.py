"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

 

示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x*x for x in A])

# go
'''
import "sort"
func sortedSquares(A []int) []int {
    var L []int
    for _, i := range A {
        L = append(L, i*i)
    }
    return sort(L)
}
'''