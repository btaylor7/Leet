# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lower = s.lower()
        letters = {}
        for letter in lower:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        return len(set(letters.values())) == 1

test = Solution()
print(test.areOccurrencesEqual("abacbc"))