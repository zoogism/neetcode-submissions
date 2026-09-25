class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        # 1, 4, 1, 2 = size 4 
        n = len(nums) # n = 4 
        ans = [0] * (2 * n) #ans = [0,0,0,0,0,0,0,0]

        for i in range(len(nums)): # first line is i = 0, num = 1
            ans[i] = nums[i]
            ans[i + n] = nums[i] # ans [0.....] = ans i+n which is right after the last element in nums which ended at index 3 so 0 + 4 = 4
            # so both the first index and the first index after the size of OG arr both get assingedf the same value 
        return ans






        