class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        if n <= 1:
            return nums[0] if n==1 else 0
        window_sum = sum(nums[:k])
        best = window_sum / k
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            avg = window_sum / k
            best = max(avg, best)
        return best