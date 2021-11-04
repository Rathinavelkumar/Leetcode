class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict={}
        for each in s:
            if each not in char_dict:
                char_dict[each] = 1
            else:
                char_dict[each] = char_dict[each] + 1

        for key, value in char_dict.items():
            if value==1: 
                return s.index(key)
        return -1