from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sortedstr = ''.join(sorted(s))
            d[sortedstr].append(s)
        result = []
        return list(d.values())

        