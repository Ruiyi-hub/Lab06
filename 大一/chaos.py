x = float(input("输入一个 0 到 1 之间的小数："))

for i in range(25):
    x = 3.9 * x - 3.9 * x * x
    print(f"{i + 1:3}  {x:.17f}")