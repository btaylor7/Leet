def plusOne(digits):
    n = len(digits)
    # Traverse the list from the last digit to the first
    for i in range(n - 1, -1, -1):
        # If the current digit is less than 9, increment it
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If it's 9, set it to 0 and move to the next digit
        digits[i] = 0
    # If all digits were 9, we need to add a new digit at the front
    return [1] + digits

test = plusOne([3,4,7,9])
print(test)