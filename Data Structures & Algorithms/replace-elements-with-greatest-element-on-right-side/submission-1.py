class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            max_value = -99999999999999
            for j in range(i +1, len(arr)):
                if arr[j] > max_value:
                    max_value = arr[j]
                arr[i] = max_value
        
        arr[len(arr) - 1] = -1

        return arr