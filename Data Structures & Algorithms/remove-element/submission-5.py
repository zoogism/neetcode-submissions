class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        res = []
        count = 0


        for num in nums:
            if num != val:
                res.append(num)
                count += 1

        for i in range(len(res)):
            nums[i] = res[i]

        return count