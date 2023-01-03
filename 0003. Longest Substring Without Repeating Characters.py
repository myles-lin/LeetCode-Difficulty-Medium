class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ''
        longest = 0
        for alpha in s:
            while alpha in string:
                string = string[1:]

            string += alpha
            longest = max(len(string), longest)
        return longest

# s = "abcabcbb" # Output: 3
# s = "bbbbb" # Output: 1
# s = "pwwkew" # Output: 3
# Solution().lengthOfLongestSubstring(s)
