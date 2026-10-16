class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_list = [c for c in s if c in vowels]
        res = [vowel_list.pop() if c in vowels else c for c in s]
        return "".join(res)