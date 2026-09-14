class Solution:
    def maxArea(self, heights: List[int]) -> int:
        longest = 0
        res = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            width = abs(L - R)
            height = min(heights[L], heights[R])
            area = width * height
            if area > longest:
                longest = area

            if (heights[L] <= heights[R]):
                L += 1
            else:
                R -= 1
        return longest


        