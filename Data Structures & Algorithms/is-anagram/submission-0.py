class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {i:s.count(i) for i in s}
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