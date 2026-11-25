class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)


        for strings in strs:
            lists = [0] * 26
            for char in strings:
                lists[ord(char) - ord('a')] += 1
            res[tuple(lists)].append(strings)
        return list(res.values())

