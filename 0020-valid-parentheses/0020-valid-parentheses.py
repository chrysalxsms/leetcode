class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 != 0:
            return False
        seen = []
        couples = {')': '(', '}':'{', ']':'['}
        for i in s:
            if i in couples.values():
                seen.append(i)
            elif i in couples.keys():
                if seen != [] and seen[-1] == couples[i]:
                    seen.pop()
                else:
                    return False
        if seen == []:
            return True
        else:
            return False