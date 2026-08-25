class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = list(s)
        count = Counter(s)
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                return False
        return True