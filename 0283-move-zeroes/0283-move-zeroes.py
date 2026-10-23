class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return nums
        left = 0
        right = left + 1
        while left < right:
            while nums[right] == 0:
                right += 1
                if right > n-1:
                    return nums
            while nums[left] != 0:
                left += 1
                if left == right:
                    if right >= n-1:
                        return nums
                    if right < n:
                        right += 1
            nums[left], nums[right] = nums[right], nums[left]
        return left
                