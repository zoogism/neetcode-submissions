class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = [[] for i in range(len(nums)+ 1)]
        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        # index will refer to count now ie 
        # if 1,1,2,2,2,3 = 
        # at index 1 = 3, at index 2 = 1, index 3 = 2
        for element, count in hashMap.items():
            freq[count].append(element)


# [], [3], [1], [2], [], [], []
        res = []

        for i in range(len(freq)-1,-1,-1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
        
    

        


         
        