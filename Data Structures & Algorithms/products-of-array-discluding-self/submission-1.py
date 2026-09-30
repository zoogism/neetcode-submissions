class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 1. Prefix product (inclusive)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        # 2. Postfix product (inclusive)
        postfix = [0] * n
        postfix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        # 3. Put the neutral 1 just outside each end
        prefix = [1] + prefix
        postfix = postfix + [1]

        # 4. Left * right for each index
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * postfix[i + 1]

        return res

        