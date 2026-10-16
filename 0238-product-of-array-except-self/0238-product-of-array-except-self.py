import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out = [1] * n

        left = 1
        for i in range(n):
            out[i] = left        # product of everything left of i
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right      # multiply in product of everything right of i
            right *= nums[i]

        return out
        