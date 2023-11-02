def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    digits.insert(0, 1)
    return digits

digits1 = [1, 2, 3]
result1 = plusOne(digits1)
print(result1)

digits2 = [9]
result2 = plusOne(digits2)
print(result2)
