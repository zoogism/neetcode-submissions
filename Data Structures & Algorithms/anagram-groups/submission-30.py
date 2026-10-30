class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)


        for elements in strs:
            count = [0] * 26
            for char in elements:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(elements)

        return list(res.values())
        