total_score = 0
num_students = 30
count = 0

while count < num_students:
    try:
        score = float(input(f"Enter the score for student {count + 1}: "))
        if score < 0 or score > 100:
            print("Invalid score, please enter again.")
            continue
        total_score += score
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid score as a number.")

if count == num_students:
    average_score = total_score / num_students
    print(f"输入完成！结果是 {average_score:.2f} points.")
