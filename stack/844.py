"""
比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        L1 = []
        for s in S:
            if s != '#':
                L1.append(s)
            else:
                if L1:
                    L1.pop()
        L2 = []
        for t in T:
            if t != '#':
                L2.append(t)
            else:
                if L2:
                    L2.pop()
        return L1 == L2