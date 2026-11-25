class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashS = {}
        hashT = {}

        for char in s:
            hashS[char] = 1 + hashS.get(char, 0)

        for char in t:
            hashT[char] = 1 + hashT.get(char, 0)
        
        return hashS == hashT

      


        