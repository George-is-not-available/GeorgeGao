import random
number = random.randint(1,100)
while True:
    try:
        huida = int(input("猜一个1至100的数字: "))
        if huida == number:
            print("恭喜您答对了")
            break
        if huida < number:
            print("太小了，要不再试试？")
        if huida > number:
            print("太大了，要不再试试？")
    except ValueError:
        print("请不要输入字符，您需要回答数字.")
