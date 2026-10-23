class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Traverse and compute the bitwise AND
        # if a and b satisfy a&b=k -> every set bit of k must also be set in both a and b
        # => the subset of the set bits in both a and b (-> a&k=k and b&k=k)
        n = len(nums)
        res = -1
        for i in range(n):
            # no swap needed
            if nums[i] == i:
                continue
            # every nums[i] where nums[i] != i must participate in at least one swap satisfying nums[i] & nums[j] = k for some index j => must satisfy nums[i]&k=k, meaning that every set bit of k must be present in all misplaced elements
            res &= nums[i]
        if res == -1:
            return 0
        else:
            return res