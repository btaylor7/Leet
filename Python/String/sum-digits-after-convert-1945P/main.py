# You are given a string s consisting of lowercase English letters, and an integer k. Your task is to convert the string into an integer by a special process, and then transform it by summing its digits repeatedly k times. More specifically, perform the following steps:

# Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
# Transform the integer by replacing it with the sum of its digits.
# Repeat the transform operation (step 2) k times in total.
# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        number_list = []
        alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}

        for letter in s:
            number_list.append((alphabet_dict[letter]))

          
        while k > 0:
            number_string = ''.join(str(num) for num in number_list)  
            number_list = [int(digit) for digit in number_string]  
            number_list = [sum(number_list)]
            k -=1
        
        return sum(number_list)




test = Solution()

print(test.getLucky('iiii',1))