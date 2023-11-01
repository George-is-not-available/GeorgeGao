def translate(str1):
    translation_table = str.maketrans('abcdefghijkmlnopqrstuvwxyzABCDEFGHIJKMLNOPQRSTUVWXYZ',
                                      'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA')
    str1 = str1.translate(translation_table)
    return str1


my_str = "abcABC"
print(translate(my_str))