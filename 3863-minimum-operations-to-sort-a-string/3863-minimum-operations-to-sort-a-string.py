class Solution:
    # CASE ANALYSIS
    def minOperations(self, s: str) -> int:
        n = len(s)
        mx, mn = max(s), min(s)

        # CASE 1
        # s is already sorted -> 0 operations
        if all(a <= b for a, b in zip(s, s[1:])):
            return 0
        
        # CASE 2
        # length of 2, not sorted -> substring length 1, sorting doesn't change anything -> return -1
        if n == 2:
            return -1

        # CASE 3
        # if first character is the smallest -> sort s[1...n-1]
        # if last char is the largest -> sort s[0...n-2]
        # 1 operation total
        if s[0] == mn or s[-1] == mx:
            return 1
        
        # CASE 4
        # largest char of s occurs only at the first position, and smallest only at the last position 
        # -> sort s[0...n-2], moving largest char to pos n-2
        # -> then sort s[n-2...n-1], largest char to pos n-1 -> CASE 3
        # -> sort s[0...n-2]
        # 3 operations total
        
        # ALL OTHER CASES
        # at least one occurrence of smallest or largest char lies in the middle of s (i, 1<=i<=n-2)
        # if the middle contains a largest char, sorting s[1...n-1] moves it to pos n-1 -> CASE 3
        # 2 operations needed total
        for i in range(1, n-1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3