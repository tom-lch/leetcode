package use_go

import "strings"

//LCP 1. 猜数字

func game(guess []int, answer []int) int {
	n := 0
	for i, val := range guess {
		if val == answer[i] {
			n ++
		}
	}
	return n
}

//771. 宝石与石头 python  return sum(S.count(i) for i in J)
func numJewelsInStones(J string, S string) int {
	n := 0
	for _, val := range S {
		for _, s := range J {
			if s == val {
				n++
			}
		}
	}
	return n
}

//1108. IP 地址无效化
// python
// class Solution:
//    def defangIPaddr(self, address: str) -> str:
//        return address.replace('.', '[.]')
func defangIPaddr(address string) string {
	r := strings.NewReplacer(".", "[.]")
	return r.Replace(address)
}

//237. 删除链表中的节点 这个题没有考虑删除的结点是最后一个
type ListNode struct {
	Val int
	Next *ListNode
}

func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}
//1252. 奇数值单元格的数目
/*
python
import numpy as np
class Solution:
def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
data = np.zeros((n, m))
for x, y in indices:
data[x, :] += 1
data[:, y] += 1
return sum(sum(data % 2 == 1))
*/

//182. 查找重复的电子邮箱
//select distinct a.Email
//from Person a, Person b
//where a.Email = b.Email and a.Id != b.Id

//709. 转换成小写字母
// go和其他高级语言类似都有 strings.ToLower(str)方法
func toLowerCase(str string) string {
	return strings.ToLower(str)
}

//832. 翻转图像
//python
//class Solution:
//    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
//        return [[j ^ 1 for j in i[::-1]] for i in A]

//1266. 访问所有点的最小时间

func minTimeToVisitAllPoints(points [][]int) int {
	if len(points) <= 1 {
		return 0
	}
	sum := 0
	for i := 1; i < len(points); i++ {
		sum +=  max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
	}
	return sum
}

func abs(x int) int {
	if x < 0 {
		return -1 * x
	}
	return x
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}
// 会有bug
