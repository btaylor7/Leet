# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = {}
        dict_t = {}

        for letter in s:
            if letter not in dict_s:
                dict_s[letter] = 1
            else:
                dict_s[letter] += 1

        for letter in t:
            if letter not in dict_t:
                dict_t[letter] = 1
            else:
                dict_t[letter] += 1
        return dict_s == dict_t
        
test = Solution()
print(test.isAnagram("anagram", "nagaramm"))
