class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        word = []
        for i in range(len(s)):
            if s[i] in vowels:
                word.append(s[i])
        reverse = word[::-1]
        v = 0
        res = ""
        for char in s:
            if char in vowels:
                res += reverse[v]
                v += 1
            else:
                res += char
        return res