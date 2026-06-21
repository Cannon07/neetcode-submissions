class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_window_len = 1 

        while right < len(s):
            window_len = right - left + 1
            substring = s[left:right + 1]
            new_char = s[right]

            char_map = {}
            for i in substring:
                if i not in char_map:
                    char_map[i] = 0
                char_map[i] += 1

            max_freq = 0
            for i in char_map:
                freq = char_map[i]
                max_freq = max(max_freq, freq)
            
            if window_len - max_freq <= k:
                right += 1
                max_window_len = max(window_len, max_window_len)
            else:
                char_map[s[left]] -= 1
                left += 1
        
        return max_window_len
            
            
    