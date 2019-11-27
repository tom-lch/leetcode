# leetcode
使用 go 解答
package use_go
import "strings"
````
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
//938. 二叉搜索树的范围和
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, L int, R int) int {
	// 方法一 ： 使用中序遍历二叉树可以得到root.val的顺序序列从L到R之间的值可以进行计算和
	//sum := 0
	//先中序遍历二叉树
	//List = seartmintree(root)
	//for _, i := range List{
	//  if i <=R && i >= L { sum += i}
	//}
	//
	// 方法二： 使用递归来计算
	if root == nil{
		return 0
	}
	if root.Val < L {
		return rangeSumBST(root.Right, L, R)
	} else if root.Val > R {
		return rangeSumBST(root.Left, L, R)
	} else {
		return root.Val +  rangeSumBST(root.Right, L, R) + rangeSumBST(root.Left, L, R)
	}
}
//1221. 分割平衡字符串
func balancedStringSplit(s string) int {
	//解题思路是遍历字符串，然后使用标志符来判断是否分割
	cont, flag := 0, 0
	for _, i := range s {
		if i == 'R'{
			flag += 1
		} else {
			flag -= 1
		}
		if flag == 0 {
			cont += 1
		}
	}
	return cont
}
// 832. 翻转图像
func flipAndInvertImage(A [][]int) [][]int {
    //此题使用暴力法来解决
    // 先遍历第一层数组，在将里面的数组翻转使用1-每个元素,也可以与1求XOR
    var B [][]int
    for _, list := range A {
        var inner []int
        for j:=len(list)-1; j >= 0 ; j-- {
            inner = append(inner, 1-list[j])
        }
        B = append(B, inner)
    }
    return B
}

//804. 唯一摩尔斯密码词
//简单的
func uniqueMorseRepresentations(words []string) int {
    // 遍历字符串数组，在遍历字符串，将每个字符转换成摩尔密码
    //将组成的摩尔密码放到字典这种，即字典的key唯一来实现去重
    moer := [26]string {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    mk := make(map[string]int)
    for _, word := range words {
        a := ""
        for _, i := range word{
            a += moer[i-'a']
        }
        mk[a] = 1
    }
    return len(mk)
}

461. 汉明距离
func hammingDistance(x int, y int) int {
    // 使用python仅一句话 return bin(x^y).count('1')
    // 本方法使用了01串的按位^或运算
    // 即可降两个串中不同的位置放在一个串中，之后统计该串中1的个数
    xor := x^y
    cont := 0
    for xor > 0 {
        // 当该串>0时，判断最后一位，010101 & 1 是否>0。如果串最后一位中含有1 则必然是>0
        if xor & 1 > 0 {
            cont ++
        }
        //判断完后穿右移一位
        xor >>= 1 // xor = xor >> 1
    }
    return cont
}

//657. 机器人能否返回原点
func judgeCircle(moves string) bool {
    //使用简单方法及使用标签符来对R-L U-D进行相互抵消
    //只遍历一遍字符串即可
    flag0, flag1 := 0, 0
    for _, i := range moves {
        if i == 'U'{
            flag0 ++
        } else if i == 'D' {
            flag0 --
        } else if i == 'R' {
            flag1 ++
        } else {
            flag1 --
        }
    }
    if flag1 == 0 && flag0 == 0{
        return true
    } else {
        return false
    }
}

//104. 二叉树的最大深度
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    // 使用传统方法，即递归遍历树 1行代码即可
    if root == nil {
        return 0
    }
    //因为go这个沙雕语言没有重载，所以math库里只有float64的Max
    return max(maxDepth(root.Right), maxDepth(root.Left)) + 1
}
// go的函数返回值的类型是个坑 以后写函数都要写上 避免遗漏出现的大坑
func max(x int, y int) int {
    if x >= y{
        return x
    } else {
        return y
    }
}

//700. 二叉搜索树中的搜索
//需要注意元素没有在树中的情况
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        return nil
    }
    if root.Val == val {
        return root
    }
    if root.Val < val {
        return searchBST(root.Right, val)
    } else {
        return searchBST(root.Left, val)
    }
}
`````

