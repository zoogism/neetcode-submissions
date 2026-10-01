class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        # -1, -1, 0, 1, 2, 4

        for a in range(len(nums)):

            if nums[a]> 0:
                break

            if a > 0 and nums[a] == nums[a-1]:
                continue

            L = a + 1
            R = len(nums)-1

            

            while L < R:
                if nums[a] + nums[L] + nums[R] > 0:
                    R -= 1
                elif nums[a] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    res.append([nums[a], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return res

        