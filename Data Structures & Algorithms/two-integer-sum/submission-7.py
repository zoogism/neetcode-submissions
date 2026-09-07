class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index


        i = 0
        prevMap = {}

        for num in nums:
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[num] = i
            i += 1




        