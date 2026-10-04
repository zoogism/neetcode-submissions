class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = [0] * len(nums)

        running_sum = 0

        for i in range(len(nums)):
            prefix[i] = running_sum
            running_sum += nums[i]
        
        suffix = [0] * len(nums)
        running_sum = 0

        for i in range(len(nums)-1,-1,-1):
            suffix[i] = running_sum
            running_sum += nums[i]

        res = []

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1
        