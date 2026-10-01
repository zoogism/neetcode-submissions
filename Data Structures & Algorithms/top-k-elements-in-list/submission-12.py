class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # = 1,1,2,2,2,3
        hashMap = {}

        freq = [[] for i in range(len(nums)+ 1)]
        # = [[],[],[],[],[],[]]

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        # = hashMap = {1:2, 2:3. 3:1} 

        for i, count in hashMap.items():
            freq[count].append(i)

        # = [[], [3], [1], [2], [], [],]

        # above is basically saying index reps count 
        # so 3 being at index 1 = it appears once, 
        # 1 at index 2 = it appears twice 
        # 2 at index 3 = it appears 

        res = []

        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if k == len(res):
                    return res

        

        