class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        iso_map = {}
        ito_map = {}
        for i, d in enumerate(s):
            if d not in iso_map:
                iso_map[d] = i
            if t[i] not in ito_map:
                ito_map[t[i]] = i
            if iso_map[d] != ito_map[t[i]]:
                return False

        return True