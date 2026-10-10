class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        prevSmaller = [-1] * len(heights)
        nextSmaller = [len(heights)] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stackTop = stack.pop()
                nextSmaller[stackTop] = i
            
            if stack:
                prevSmaller[i] = stack[-1]
            
            stack.append(i)

        
        maxArea = 0
        for i in range(len(heights)):
            currentHeight = heights[i]
            width = nextSmaller[i] - prevSmaller[i] -1
            maxArea = max(maxArea, currentHeight * width)
        
        return maxArea
        


        



        