class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            sort_dict[sorted_word].append(s)
        return list(sort_dict.values())
        
