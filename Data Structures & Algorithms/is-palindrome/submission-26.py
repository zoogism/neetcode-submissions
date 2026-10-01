class Solution:
    def isPalindrome(self, s: str) -> bool:


        L = 0
        R = len(s) - 1

        while L < R:

            while L < R and not self.isAlphanumeric(s[L]):
                L += 1
            while R > L and not self.isAlphanumeric(s[R]):
                R -= 1
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
            else:
                return False
        
        return True


            


    

    def isAlphanumeric(self,c):
        return (ord('a') <= ord(c) <= ord('z') 
        or ord('A') <= ord(c) <= ord('Z')
        or ord('0') <= ord(c) <= ord('9')  )

        
        