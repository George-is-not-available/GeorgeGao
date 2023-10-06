age = 25

if age < 1:
    print("The person is a baby.")
elif age >= 1 and age <= 2:
    print("The person is a toddler.")
elif age >= 3 and age <= 12:
    print("The person is a child.")
elif age >= 13 and age <= 20:
    print("The person is a teenager.")
elif age >= 21 and age <= 24:
    print("The person is a youngster.")
elif 25 <= age <= 64:
    print("The person is an adult.")
else:
    print("The person is a senior.")
