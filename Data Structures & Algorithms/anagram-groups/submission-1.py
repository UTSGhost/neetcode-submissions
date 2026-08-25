class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # anagram sorted -> string list
        for s in strs:
            sortedstr = ''.join(sorted(s))
            if sortedstr in d:
                d[sortedstr].append(s)
            else:
                d[sortedstr] = [s]
        result = []
        for li in d:
            result.append(d[li])
        return result

        