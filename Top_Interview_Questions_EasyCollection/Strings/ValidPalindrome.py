class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_1 = "".join([ each.lower() for each in s if each.isalnum() ])
        str_2 = str_1[::-1]
        
        return str_1==str_2