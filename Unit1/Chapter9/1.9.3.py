def remove_characters(string1, remove_character):
    string_list = []
    for i in range(len(string1) - 1):
        string_list.append(string1[i])
    for r in range(len(remove_character) - 1):
        list_index = string_list.index(remove_character[r])
        string_list.pop(list_index)
    string_list = ''.join(string_list)
    return string_list


my_str = "They are fucking niggers."
remove_list = 'aeinu'
print(remove_characters(my_str, remove_list))