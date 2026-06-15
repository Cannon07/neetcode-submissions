class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        enumerate_strs = []
        hash_map = {}
        result = []
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in hash_map:
                hash_map[sorted_string] = []
            hash_map[sorted_string].append(string)
        for i in hash_map:
            result.append(hash_map[i])
        return result