class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        result = list(groups.values())
        # for group in result:
        #     group.sort()
        # result.sort(key=lambda g: (len(g), g))
        return result