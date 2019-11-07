"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-characters-by-frequency
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 使用python做题不太合适
class Solution:
    def frequencySort(self, s: str) -> str:
        S = ''
        print(s)
        ss = list(set(list(s)))
        zz = []
        for _ in ss:
            zz.append(0)
        dict_s = dict(zip(ss, zz))
        for i in s:
            dict_s[i] += 1
        for i in sorted(dict_s, key=dict_s.__getitem__, reverse=True):
            S += i*dict_s[i]
        return S