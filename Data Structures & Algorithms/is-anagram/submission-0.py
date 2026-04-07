from collections import Counter
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        char_s = Counter(s)
        char_t = Counter(t)
        return char_s == char_t
        

        