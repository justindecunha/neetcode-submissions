from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in freq.items():
            buckets[val].append(key)
        
        res = []
        for bucket in reversed(buckets):
            for i in bucket:
                res.append(i)
                if len(res) == k:
                    return res


