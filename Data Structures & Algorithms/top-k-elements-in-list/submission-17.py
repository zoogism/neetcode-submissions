class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, freq in count.items():
            bucket[freq].append(num)

        
        res = []

        for i in range(len(bucket)-1, -1, -1):
            for element in bucket[i]:
                res.append(element)
                if len(res) == k:
                    return res


        