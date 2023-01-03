from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            lst[sorted_word].append(word)
        return lst.values()
    
# strs = ["eat","tea","tan","ate","nat","bat"] # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Solution().groupAnagrams(strs)
