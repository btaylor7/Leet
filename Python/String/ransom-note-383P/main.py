# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        new_string = ""
        for letter in ransomNote:
            if letter in magazine:
                first_occurence = magazine.index(letter)
                magazine = magazine[:first_occurence] + magazine[first_occurence+1:]
                new_string += letter
        return new_string == ransomNote


test = Solution()
print(test.canConstruct("aa","aab"))
#Happy with this one :)