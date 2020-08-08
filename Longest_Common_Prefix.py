from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs) # number of words
        if m < 1:
            return ''
        elif m is 1:
             return strs[0]
        mi = 10000000
        for i in range(m):
            mi = min(mi, len(strs[i]))
        ans = ''
        if mi is 0:
            return ''
        i = 0
        while True:
            if not i < mi:
                break
            if len(strs[0]) is 0:
                return ans
            c = strs[0][i]
            flag = False
            for j in range(1, m):
                if strs[j][i] is c:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                ans += c
            else:
                break
            i += 1
        return ans
                
                