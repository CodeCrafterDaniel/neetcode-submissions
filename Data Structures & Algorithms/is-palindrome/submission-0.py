class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = ''
        for letter in s:
            if letter.isalnum():
                clear_s += letter.lower()
        
        l, r = 0, len(clear_s) - 1 

        print(clear_s)
        while l < r:
            if clear_s[l] != clear_s[r]:
                return False
            l += 1
            r -= 1
        
        return True