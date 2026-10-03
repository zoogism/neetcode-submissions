class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        total = 0

        while L < R:
            if maxL <= maxR:
                L += 1
                water = maxL - height[L]
                if water > 0:
                    total += water
                if height[L] > maxL:
                    maxL = height[L]
            else:
                R -= 1
                water = maxR - height[R]
                if water > 0:
                    total += water
                if height[R] > maxR:
                    maxR = height[R]

        return total