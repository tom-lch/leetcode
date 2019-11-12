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

