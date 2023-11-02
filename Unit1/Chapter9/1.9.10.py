def romanToInt(s):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1 or roman_to_int[s[i]] >= roman_to_int[s[i + 1]]:
            result += roman_to_int[s[i]]
            i += 1
        else:
            result += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
            i += 2
    return result
s1 = "III"
result1 = romanToInt(s1)
print(result1)
s2 = "LVIII"
result2 = romanToInt(s2)
print(result2)

s3 = "MCMXCIV"
result3 = romanToInt(s3)
print(result3)