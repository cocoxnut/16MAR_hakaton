t1 = int(input("Введите число 10: "))
t1 -= 1
t2 = 0
while t1 != 0:
    if (t1 % 3 == 0) or (t1 % 5 == 0):
        t2 += t1
        t1 -= 1
        print("Итоговое значение:", t2)

    else:
        print('Error')