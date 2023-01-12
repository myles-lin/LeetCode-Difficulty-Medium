class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return ' '.join(s)
        # return ' '.join(reversed(s.split()))

# s = "the sky is blue"# Output: "blue is sky the"
# s = "  hello world  " # Output: "world hello"
# s = "a good   example" # Output: "example good a"
# Solution().reverseWords(s)
