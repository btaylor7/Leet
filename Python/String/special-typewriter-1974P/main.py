# Each second, you may perform one of the following operations:

# Move the pointer one character counterclockwise or clockwise.
# Type the character the pointer is currently on.
# Given a string word, return the minimum number of seconds to type out the characters in word.

 

# Example 1:

# Input: word = "abc"
# Output: 5
# Explanation: 
# The characters are printed as follows:
# - Type the character 'a' in 1 second since the pointer is initially on 'a'.
# - Move the pointer clockwise to 'b' in 1 second.
# - Type the character 'b' in 1 second.
# - Move the pointer clockwise to 'c' in 1 second.
# - Type the character 'c' in 1 second.


class Solution:
    def minTimeToType(self, word: str) -> int:
        count = 0
        alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
        current = alphabet_dict['a']

        for letter in word:
            distance = abs(current - alphabet_dict[letter])
            count += min(distance, 26 - distance) + 1 #26-distance ensures overlaps are counted as 1, eg z to a is distance of 1.
            current = alphabet_dict[letter]

        return count

    
test = Solution()

print(test.minTimeToType('bza'))

           

