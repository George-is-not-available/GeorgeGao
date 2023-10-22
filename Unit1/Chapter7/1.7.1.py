month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
list_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i = 0
while i <= 11:
    print(f"{month[i]} has {list_non_leap[i]} days in common years and {list_leap[i]} days in leap years")
    i += 1