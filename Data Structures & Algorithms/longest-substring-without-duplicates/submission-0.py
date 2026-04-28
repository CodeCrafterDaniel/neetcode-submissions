class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_letters = set()
        max_len = 0

        l = 0
        for r in range(len(s)):
            print(cur_letters)
            if s[r] not in cur_letters:
                cur_letters.add(s[r])
            else:
                while s[r] in cur_letters:
                    cur_letters.remove(s[l])
                    l += 1
                cur_letters.add(s[r])

            max_len = max(max_len, len(cur_letters))
        
        return max_len
            