class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        flag=True

        if len(s)==len(t):
            s_dict={}
            for each in s:
                if each not in s_dict:
                    s_dict[each] = 1
                else:
                    s_dict[each] = s_dict[each] + 1
            print(s_dict)

            t_dict={}
            for each in t:
                if each not in t_dict:
                    t_dict[each] = 1
                else:
                    t_dict[each] = t_dict[each] + 1
            print(t_dict)

            for each in s_dict.keys():
                if each in t_dict:
                    if t_dict[each]!=s_dict[each]:
                        flag=False
                else:
                    flag=False
        else:
            flag=False

        return flag