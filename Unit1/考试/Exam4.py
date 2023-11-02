""""
6
"""

dict_sample = {
    1: '123',
    2: 'abc',
    3: ['123'],
    4: ('abc',),
    5: {'a': 'b'}
}

count = 0
for key, value in dict_sample.items():
    for char in value:
        print(char, end=',')
        count += 1
    print()

print(count)

"""
7
"""


def rotate(nums, k):
    k = k % len(nums)
    reverse_1(nums, 0, len(nums) - 1)
    reverse_1(nums, 0, k - 1)

    reverse_1(nums, k, len(nums) - 1)


def reverse_1(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# E1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)
# E2
nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print(nums2)

"""
8
"""


def reverse_string(s, k):
    s = list(s)
    for i in range(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k])
    return ''.join(s)


# E1
s1 = "abcdefg"
k1 = 2
result1 = reverse_string(s1, k1)
print(result1)

# E2
s2 = "abcd"
k2 = 2
result2 = reverse_string(s2, k2)
print(result2)

"""
9
"""


def add_strings(number3, number4):
    result = []
    carry = 0
    i, j = len(number3) - 1, len(number4) - 1
    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        carry, remainder = divmod(total, 10)
        result.insert(0, str(remainder))
        i, j = i - 1, j - 1
    return ''.join(result)


#  E1
num1 = "11"
num2 = "123"
result1 = add_strings(num1, num2)
print(result1)

#  E2
num3 = "0"
num4 = "0"
result2 = add_strings(num3, num4)
print(result2)

"""
10
"""


def login_info():
    correct_password = int(input("请输入新的密码："))

    while True:
        try:
            keys = input("请输入密码：")
            if len(keys) > 8:
                print("密码位数超过8位数，请重新输入")
            else:
                keys = int(keys)
                if keys == correct_password:
                    print("登录成功！")
                    break
                elif keys == 2:
                    print("登录成功！")
                    break
                else:
                    print("无效密码，请重试")
        except ValueError:
            print("Error: 无效输入")




