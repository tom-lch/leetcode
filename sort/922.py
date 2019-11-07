"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        '''
        #效率低下
        o = 0
        j = 1
        L = copy.copy(A)
        for i in A:
            if i % 2:
                L[j] = i
                j += 2
            else:
                print(L)
                L[o] = i
                o += 2
        return L
        '''
        o = [i for i in A if not i % 2]
        j = [i for i in A if i % 2]
        return [i for n in zip(o, j) for i in n]


