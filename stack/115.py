"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
        self.L_min = []
    def push(self, x: int) -> None:
        self.L.append(x)
        self.L_min.append(x)
        self.L_min.sort(reverse=True)

    def pop(self) -> None:
        a = self.L.pop()
        self.L_min.remove(a)
        return a

    def top(self) -> int:
        return self.L[-1]

    def getMin(self) -> int:
        return self.L_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()