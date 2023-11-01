def count_characters(string):
    letter_count = 0
    space_count = 0
    digit_count = 0
    other_count = 0

    for char in string:
        if char.isalpha():
            letter_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    counts = {
        "letters": letter_count,
        "spaces": space_count,
        "digits": digit_count,
        "other": other_count
    }

    return counts


input_string = "Hello, 123 world!"
result = count_characters(input_string)
print(result)