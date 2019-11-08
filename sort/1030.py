"""
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

 

示例 1：

输入：R = 1, C = 2, r0 = 0, c0 = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# python中可以用一行代码解决其他语言的是多行代码 但是这个代码所有的是sorted函数来解决数组排序的问题
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """
        #这个方法写的代码太杂碎 需要重新整理化简
        l = 0
        L = []
        r = []
        for i in range(R):
            for j in range(C):
                l = abs(r0-i) + abs(c0-j)
                L.append((l, [i, j]))
        L.sort()
        for n in L:
            r.append(n[1])
        return r
        """
        return sorted(((i, j) for i in range(R) for j in range(C)), key=lambda l:abs(l[0]-r0)+abs(l[1]-c0))