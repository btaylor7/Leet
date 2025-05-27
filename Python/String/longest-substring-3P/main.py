"""
Given a string, s, find the length of the longest substring without repeating characters.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_set = set()

        for letter in range(len(s)):

            while s[letter] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[letter])

            max_len = max(max_len, letter - left + 1)