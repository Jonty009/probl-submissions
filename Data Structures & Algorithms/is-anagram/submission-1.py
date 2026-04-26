class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        for char in s:
            s_hashmap[char] = s_hashmap.get(char, 0) + 1
        # origin = s_hashmap.copy()
        for i in t:
            if i in s_hashmap.keys():
                if s_hashmap[i] > 0:
                    s_hashmap[i] -= 1
                    continue
                else:
                    return False
            else:
                return False
        if len([i for i in s_hashmap.values() if i != 0 ]):
            return False
        else:
             return True