class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        v1_len, v2_len = len(v1), len(v2)
        max_len = max(v1_len, v2_len)
        for i in range(max_len):
            c1 = int(v1[i]) if i < v1_len else 0
            c2 = int(v2[i]) if i < v2_len else 0
            if c1 > c2: return 1
            elif c1 < c2: return -1
        return 0

# version1, version2 = "1.0", "1.0.0" # Output: 0
# version1, version2 = "1.0.1", "1" # Output: 1
# version1, version2 = "1.0.01", "1.1" # Output: -1
# Solution().compareVersion(version1, version2)

