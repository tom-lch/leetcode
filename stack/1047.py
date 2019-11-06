"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，
这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，
其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
 
提示：
1 <= S.length <= 20000
S 仅由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        #由题，S中全部都是小写字母且删去相邻元素后再检查是否有相同的元素，重复检查，直至没有相同元素。
        # 递归
        '''
        # 有bug
        if 'aa' not in S and 'bb' not in S:
            return S
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                n_S = S[:i]+S[i+2:]
                break
        return self.removeDuplicates(n_S)
        '''
        # 使用栈来实现
        L = []
        for s in S:
            L.append(s)
            if len(L)>1 and L[-1]==L[-2]:
                L.pop()
                L.pop()
        return ''.join(L)