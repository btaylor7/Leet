# Example 1:
#
# Input: s = "egg", t = "add"
#
# Output: true
#
# Explanation:
#
# The strings s and t can be made identical by:
#
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:
#
# Input: s = "foo", t = "bar"
#
# Output: false
#
# Explanation:
#
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):

            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


test = Solution()
print(test.isIsomorphic("egg", "boo"))