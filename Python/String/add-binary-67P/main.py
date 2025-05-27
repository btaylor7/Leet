# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Hardcoded but it works.
        
        len_a = len(a)
        len_b = len(b)

        if len_a > len_b:
            distance = len_a-len_b         
            b = '0'*distance + b
         
        elif len_b > len_a:
            distance = len_b-len_a
            a = '0'*distance + a
          
        else:
            print("Same length.")

        result = ''
        carry = False

        for i in range(len(a) - 1, -1, -1):  # Iterate from right to left

            if a[i] == '0':
                if b[i] == '0' and not carry:  # if a0 and b0 no carry
                    sum = '0'
                    carry = False
                elif b[i] == '1' and not carry:  # if a0 and b1 no carry
                    sum = '1'
                    carry = False
                elif b[i] == '0' and carry:  # if a0 and b0 with carry
                    sum = '1'
                    carry = False
                elif b[i] == '1' and carry:  # if a0 and b1 with carry
                    sum = '0'
                    carry = True
            else:
                if b[i] == '0' and not carry:  # if a1 and b0 no carry
                    sum = '1'
                    carry = False
                elif b[i] == '0' and carry:  # if a1 and b0 with carry
                    sum = '0'
                    carry = True
                elif b[i] == '1' and carry:  # if a1 and b1 with carry
                    sum = '1'
                    carry = True
                elif b[i] == '1' and not carry:  # if a1 and b1 no carry
                    sum = '0'
                    carry = True
            result = sum + result

        if carry:
            result = '1' + result

        return result

                     

                  



       

test = Solution()

print(test.addBinary("11","1"))
        