import random


def guess_the_number():
    print("欢迎来到猜数字游戏！")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("猜一个1到100之间的整数："))
            attempts += 1

            if guess < secret_number:
                print("太小了，再试一次。")
            elif guess > secret_number:
                print("太大了，再试一次。")
            else:
                print(f"恭喜你，你猜对了！答案是{secret_number}。你用了{attempts}次尝试。")
                break
        except ValueError:
            print("请输入有效的整数。")


guess_the_number()

# print(Hello world)