import math

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выйти из программы")

    vibor = input()

    if vibor == "11":
        print("Программа завершена.")
        break

    try:
        if vibor in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
            cifr1 = float(input("Введите первое число: "))

        if vibor in ("1", "2", "3", "4", "5"):
            cifr2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Введите корректное число.")
        continue
    if vibor == "1":
        rez = cifr1 + cifr2
        print("Результат: ", rez)
    elif vibor == "2":
        rez = cifr1 - cifr2
        print("Результат: ", rez)
    elif vibor == "3":
        rez = cifr1 * cifr2
        print("Результат: ", rez)
    elif vibor == "4":
        if cifr2 == 0:
            print("Ошибка: Деление на ноль.")
        rez = cifr1 / cifr2
        print("Результат: ", rez)
    elif vibor == "5":
        rez = cifr1 ** cifr2
        print("Результат: ", rez)
    elif vibor == "6":
        if cifr1 < 0:
            print("Ошибка: Нельзя извлечь квадратный корень из отрицательного числа.")
            continue
        rez = math.sqrt(cifr1)
        print("Результат: ", rez)
    elif vibor == "7":
        rez = math.factorial(int(cifr1))
        print("Результат: ", rez)
    elif vibor == "8":
        rez = math.sin(math.radians(cifr1))
        print("Результат: ", rez)
    elif vibor == "9":
        rez = math.cos(math.radians(cifr1))
        print("Результат: ", rez)
    elif vibor == "10":
        rez = math.tan(math.radians(cifr1))
        print("Результат: ", rez)
    else:
        print("Ошибка: Неправильный выбор операции.")
