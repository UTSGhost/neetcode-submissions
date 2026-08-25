from collections import defaultdict
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=lambda x: counts[x])
