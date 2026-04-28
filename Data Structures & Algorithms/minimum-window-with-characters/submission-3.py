from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        cnt_need = Counter(t)
        cnt_cur = Counter(s[:len(t)])

        matches = 0

        for el in cnt_need:
            if el in cnt_cur and cnt_cur[el] >= cnt_need[el]:
                matches += 1
        
        if matches == len(cnt_need):
            return s[:len(t)]

        l = 0
        min_len = 10**10
        sub = ''

        for r in range(len(t), len(s)):
            cur_el = s[r]

            if cur_el in cnt_need:
                cnt_cur[cur_el] = cnt_cur.get(cur_el, 0) + 1

                if cnt_cur[cur_el] == cnt_need[cur_el]:
                    matches += 1
            print(matches)
            while matches >= len(cnt_need):
                print(l)
                cnt_cur[s[l]] -= 1

                if s[l] in cnt_need:
                    if cnt_cur[s[l]] == cnt_need[s[l]] - 1:
                        matches -= 1

                l += 1

                if min_len > r - l + 2:
                    min_len = r-l+2
                    sub = s[l-1:r+1]
            
        return sub
            

