class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        # 0,0,0

        for n in nums:
            count[n] += 1
        
        i = 0

        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i+= 1
        return nums

        # result = [1,2,1] 
        # at index 0 which reps red = 1
        # at index 1 which reps white = 2
        # at index 2 which reps blue = 1