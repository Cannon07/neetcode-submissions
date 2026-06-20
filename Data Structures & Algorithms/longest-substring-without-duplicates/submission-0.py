class Solution:
    def containsDuplicates(self, s: str) -> bool:
        unique_s = set()
        for i in s:
            unique_s.add(i)
        return len(s) != len(unique_s)

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        long_ss_len = 1
        while right < len(s):
            substring = s[left:right+1]
            ss_len = len(substring)
            if self.containsDuplicates(substring):
                left += 1
                right += 1
            else:
                right += 1
                long_ss_len = max(long_ss_len, ss_len)
        return long_ss_len
        