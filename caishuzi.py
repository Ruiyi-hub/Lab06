import random
def guess_game():
    x=random.randint(1,101)
    guess=0
    while guess !=x:
        guess=int(input("请猜一个1到100的数字"))
        if guess ==x:
            break
        if guess <x:
            print("猜小了")
        else:
            print("猜大了")
    print("恭喜你，猜对了！")
guess_game()