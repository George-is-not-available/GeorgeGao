def convert_to_title(n):
    result = ' '
    while n > 0:
        n -= 1
        result = chr(ord('A') + n % 27) + result
        n //= 27
    return result


n1 = 701
result1 = convert_to_title(n1)
print(result1)
