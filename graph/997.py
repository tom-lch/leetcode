"""
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-town-judge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        a = [0 for x in range(N+1)]
        b = [0 for x in range(N+1)]
        # trust[0] 新任别人的人 trust[1]被人信任的人
        for num in trust:
            a[num[0]] += 1
            b[num[1]] += 1

        for i, num in enumerate(b):
            if i != 0 and num == N-1:
                if a[i] == 0:
                    return i
        return -1