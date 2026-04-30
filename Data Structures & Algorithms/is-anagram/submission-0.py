class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # abracadabra
        # caradbaaabr

        if len(s) != len(t):
            return False
        
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for c in t:

            if c not in freq.keys():
                return False
            
            if freq[c] <= 0:
                return False
            else:
                freq[c] = freq[c] - 1
        
        return True
