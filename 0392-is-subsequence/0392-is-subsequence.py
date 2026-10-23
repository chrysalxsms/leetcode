class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if len(t) <= 1:
            return True if s == t else False
        left = 0
        right = 0
        while left < len(s):
            if right >= len(t): 
                return False
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1
        return True