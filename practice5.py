from math import factorial, comb


def menu():
    """Отображает меню действий."""
    print("\n-----------СУПЕР МЕНЮ-----------")
    print("1. Ряд Маклорена с косинусом")
    print("2. Ряд Маклорена с биноминальным коэффициентом")
    print("3. Выход из программы")


def cos_macloren(n):
    while True:
        try:
            x = float(input("Введите значение x для косинуса: "))
            break
        except ValueError:
            print("Введите целочисленные данные х")
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result


def maclaurin_series(n, m):
    while True:
        try:
            x = float(input("Введите значение x (-1 < x < 1): "))
            if x <= -1 or x >= 1:
                print("Значение x должно быть в диапазоне (-1, 1). Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Введите корректные данные.")

    result = 0
    for i in range(n):
        binomial_coefficient = comb(m, i)  # Используем comb для вычисления биномиального коэффициента
        result += binomial_coefficient * (x ** i)

    return result


def main():
    while True:
        menu()
        n = 15
        try:
            choice = input("Введите целочисленное значение выбора меню: ")
            if choice == "1":
                result = cos_macloren(n)
                print(f"Приближение косинуса: {result}")
            elif choice == "2":
                m = int(input('Введите степень m: '))
                result = maclaurin_series(n, m)
                print(f"Приближение ряда Маклорена: {result}")
            elif choice == "3":
                break
            else:
                print("Неверный выбор, попробуйте снова.")
        except ValueError:
            print("Введите целочисленные данные выбора меню")


if __name__ == "__main__":
    main()
