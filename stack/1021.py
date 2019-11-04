# leetcode
# 1021. 删除最外层的括号
# 方案一
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        start = 0
        index = 0
        s = ''
        for i in range(len(S)):
            if S[i] == '(':
                start += 1
            if S[i] == ')':
                start -= 1
            if S[i] == '(' and start == 1:
                index = i
            if start == 0:
                s += S[index+1: i]
        return s
