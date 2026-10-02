class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1 
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                temp = nums[i]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1
        
        return j



        



        