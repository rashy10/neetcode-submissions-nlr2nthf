class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        b = [0]*26
        if len(s) != len(t):
            return False

        for i in range(len(t)):
            a[ord(s[i])-ord('a')] += 1
            b[ord(t[i])-ord('a')] += 1

        return a == b 
        
        