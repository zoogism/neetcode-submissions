class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # indices of temperatures, kept in decreasing order

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res