class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n_map = {}
        for n in nums:
            if n in n_map.keys():
                n_map[n] += 1
            else:
                n_map[n] = 1
        return sorted(n_map, key = n_map.get, reverse=True)[:k]


        