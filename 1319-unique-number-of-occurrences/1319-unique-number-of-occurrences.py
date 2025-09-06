from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=defaultdict(int)
        for num in arr:
            freq[num]=freq.get(num,0)+1
        return len(set(freq.keys()))==len(set(freq.values()))
        