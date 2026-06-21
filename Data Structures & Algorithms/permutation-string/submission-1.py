class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_char_map = {}
        s2_sub_char_map = {}

        for i in range(len(s1)):
            if s1[i] not in s1_char_map:
                s1_char_map[s1[i]] = 0
            s1_char_map[s1[i]] += 1

            if s2[i] not in s2_sub_char_map:
                s2_sub_char_map[s2[i]] = 0 
            s2_sub_char_map[s2[i]] += 1
            
        if s1_char_map == s2_sub_char_map:
            return True

        left = 0  
        right = len(s1) - 1

        while right < len(s2) - 1:
            s2_sub_char_map[s2[left]] -= 1
            if s2_sub_char_map[s2[left]] == 0:
                del s2_sub_char_map[s2[left]]
            left += 1

            right += 1
            if s2[right] not in s2_sub_char_map:
                s2_sub_char_map[s2[right]] = 0
            s2_sub_char_map[s2[right]] += 1

            if s1_char_map == s2_sub_char_map:
                return True
            
        return False
        