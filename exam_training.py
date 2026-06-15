"""
Exam Training — 15 June 2026
Preparation for Stepik Python Basics exam

Topics covered:
- input() / print() / sep / end
- Variables, PEP8
- Integer arithmetic: +, -, *, **, //, %
- Digit extraction algorithms
- Priority of operations
- Edge cases (negative numbers, ZeroDivisionError)

Result: 15/15 tasks solved correctly
"""
  # Задача №15 - Дано четырёхзначное число. Выведи: Сумму первой и последней цифры, разность второй и третьей цифры, произведение всех цифр.
num = int(input())
digit1 = num // 10 ** 3
digit2 = (num // 10 ** 2) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
print(digit1 + digit4)
print(digit2 - digit3)
print(digit1 * digit2 * digit3 * digit4)

  # Задача №14 - Что выведет код? - Ответ: 25, 40, 65
a, b, c = int(input()), int(input()), int(input())
a = b + c
b = a + c
c = a + b
print(a, b, c)

  # Задача №13 - Что выведет код? Если будет ошибка — напиши "Error". - Error
a = 15 % (16 // 7)
b = 20 // (5 % 5)
print(a + b)

  # Задача №12 - Дано число n. Выведи n ** 2 и n ** 3. Но n может быть большим (до 1000).
num = int(input())
print(num ** 2)
print(num ** 3)

  # Задача №11 - Дано трёхзначное число. Выведи результат: (первая цифра * последняя цифра) + средняя цифра.
num = int(input())
digit1 = num // 10 ** 2
digit2 = (num // 10) % 10
digit3 = num % 10
print((digit1 * digit3) + digit2)

  # Задача №10 - Что выведет код? Напиши ответ. - Ответ - 36
a = 20 // 6 % 4
b = 3 ** 2 * 2
c = 15 // (7 % 3)
print(a + b + c)

  # Задача №9 - Дано число n (может быть отрицательным). Выведи результат n // 4 и n % 4.
num = int(input())
num_1 = (num) // 4
num_2 = (num) % 4
print(num_1)
print(num_2)

  # Задача №8 - Дано двузначное число. Выведи сумму цифр и их произведение в двух строках.
num = int(input())
digit1 = num // 10
digit2 = num % 10
print(f"Сумма: {digit1 + digit2}")
print(f"Произведение: {digit1 * digit2}")

  # Задача №7 - Дано число n. Выведи предпоследнюю цифру числа.
num = int(input())
digit_last = (num // 10) % 10
print(digit_last)

  # Задача №6 -  Дано трёхзначное число. Выведи число, образованное перестановкой первой и последней цифры.
num = int(input())
digit1 = num // 10 ** 2
digit2 = (num // 10) % 10
digit3 = num % 10
print(digit3, digit2, digit1, sep = "")

  # Задача №5 - Дано число секунд. Выведи, сколько это часов, минут и секунд.
num = int(input())
digit1 = num // 60 ** 2
digit2 = (num // 60) % 60
digit3 = num % 60
print(f"Часов: {digit1}")
print(f"Минут: {digit2}")
print(f"Секунд: {digit3}")

  # Задача №4 - Дано четырёхзначное число. Выведи сумму первой и последней цифры.
num = int(input())
digit1 = num // 10 ** 3
digit2 = (num // 10 ** 2) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
print(digit1 + digit4)  

  # Задача №3 - Дано число n. Выведи последние две цифры этого числа.
num = int(input())
digit_last = num % 10
digit_next = (num // 10) % 10
print(digit_next, digit_last, sep = "")

  # Задача №2 - Дано трёхзначное число. Выведи произведение его цифр.
num = int(input())
digit1 = num // 10 ** 2
digit2 = (num // 10) % 10
digit3 = num % 10
print(digit1 * digit2 * digit3)  

  # Задача №1 - Дано двузначное число. Выведи число, образованное перестановкой цифр местами.
num = int(input())
digit1 = num // 10
digit2 = num % 10
print(digit2, digit1, sep = "")  
