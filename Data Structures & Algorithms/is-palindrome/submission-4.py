class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                string += i
        l = 0
        r = len(string) -1
        string = string.lower()
        print(string)
        while l <= r:
            if string[l] != string[r]:
                return False

            l += 1
            r -= 1
        return True
        