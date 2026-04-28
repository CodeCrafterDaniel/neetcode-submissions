from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:len(s1)])
        matches = 0

        for el in cnt1:
            if el in cnt2 and cnt1[el] == cnt2[el]:
                matches += 1
        
        if matches == len(cnt1):
            return True
        
        for i in range(len(s1), len(s2)):
            right = s2[i]
            left = s2[i - len(s1)]

            cnt2[right] = cnt2.get(right, 0) + 1
            if right in cnt1:
                if cnt2[right] == cnt1[right]:
                    matches += 1
                elif cnt2[right] == cnt1[right] + 1:
                    matches -= 1

            cnt2[left] -= 1
            if left in cnt1:
                if cnt2[left] == cnt1[left]:
                    matches += 1
                elif cnt2[left] == cnt1[left] - 1:
                    matches -= 1

            if matches == len(cnt1):
                return True
        
        return False