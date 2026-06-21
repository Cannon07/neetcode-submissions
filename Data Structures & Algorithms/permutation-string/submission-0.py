class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_char_map = {}
        for i in s1:
            if i not in s1_char_map:
                s1_char_map[i] = 0
            s1_char_map[i] += 1

        left = 0
        right = len(s1) - 1
        
        while right < len(s2):
            substring = s2[left:right + 1]

            s2_sub_char_map = {}
            for i in substring:
                if i not in s2_sub_char_map:
                    s2_sub_char_map[i] = 0
                s2_sub_char_map[i] += 1
            
            if s1_char_map == s2_sub_char_map:
                return True
            
            left += 1
            right += 1
        return False
        