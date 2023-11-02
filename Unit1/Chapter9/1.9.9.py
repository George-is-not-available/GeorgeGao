def addBinary(a, b):
    result = []
    carry = 0  # 进位初始为0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        current_sum = digit_a + digit_b + carry
        carry = current_sum // 2
        result.append(str(current_sum % 2))
        i -= 1
        j -= 1
    if carry:
        result.append('1')
    return ''.join(result[::-1])
a1 = "11"
b1 = "1"
result1 = addBinary(a1, b1)
print(result1)

a2 = "1010"
b2 = "1011"
result2 = addBinary(a2, b2)
print(result2)
