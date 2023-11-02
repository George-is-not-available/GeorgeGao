def isPalindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]
s1 = "A man, a plan, a canal: Panama"
result1 = isPalindrome(s1)
print(result1)  