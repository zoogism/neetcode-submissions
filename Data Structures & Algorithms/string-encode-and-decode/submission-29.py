class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ''

        for s in strs:
            output += str(len(s)) + '#' + s
        
        return output 

  # 4#NEET4#CODE

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            to = j + 1
            From = j + 1 + length
            res.append(s[to: From])

            i = From

        return res
















        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        
        return res

            

            
            








            



      