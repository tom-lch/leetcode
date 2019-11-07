"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-stone-weight
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
#此题很简单 使用python排序 sort()  --> [1, 3 ,5 ,6, 7]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #使用python内置的排序
        if len(stones) < 2:
            return stones[0]
        stones.sort()
        while len(stones) > 1:
            #'可以更简单一些'
            """
            val = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()
            """
            val = stones.pop() - stones.pop()
            if val > 0:
                stones.append(val)
                stones.sort()
        return stones[0] if stones != [] else 0