from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groupings = defaultdict(list)

        for s in strs:
            
            s_count = [0] * 26
            for c in s:
                s_count[ord(c) - ord('a')] += 1
            anagram_groupings[tuple(s_count)].append(s)

        return [group for group in anagram_groupings.values()]


        