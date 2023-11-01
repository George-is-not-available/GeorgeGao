def check_palindrome(string_1):
    if len(string_1) % 2 == 0:
        i = 0
        s = 0
        while i <= len(string_1) - 1:
            if string_1[s] == string_1[-(s + 1)]:
                s += 1
            i += 1
            if s == len(string_1) - 1:
                return True
            elif i == len(string_1):
                return False
    else:
        string_list = list(string_1)
        i = 0
        s = 0
        while i <= len(string_1) - 1:
            if string_1[s] == string_1[-(s + 1)]:
                s += 1
            i += 1
            if s == len(string_1) - 1:
                return True
            elif i == len(string_1):
                return False


my_string = "125321"
if check_palindrome(my_string):
    print("String is a palindrome")
else:
    print("String is not a Palindrome")