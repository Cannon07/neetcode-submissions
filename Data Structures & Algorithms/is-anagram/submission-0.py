class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        len_s = len(s);
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        for i in range(len_s):
            if sorted_s[i] != sorted_t[i]:
                return False
        
        return True
