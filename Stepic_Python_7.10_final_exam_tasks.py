"""
Stepik: Python Programming
Topic: Final Exam — Code Review, Pattern Generation, and Algorithmic Optimization
Date: 15 August 2026
Status: Completed ✅ (Exam Passed)

Tasks solved: 7 (Ревью кода-7, Ревью кода-8, Ревью кода-9, Звёздная рамка, Третья цифра, Все вместе 2, Числа Рамануджана)
Topics covered:
- Debugging and refactoring pre-written code (handling edge cases, correct initialization of max/min values).
- Mathematical digit extraction (e.g., finding the N-th digit via powers of 10).
- Complex multi-condition processing consolidated into a single efficient `while` loop.
- Nested loops optimization (Ramanujan numbers: eliminating duplicate permutations via strict ascending range boundaries).

Notable challenges:
- Task "Числа Рамануджана": Successfully optimized the 4-nested-loop search by enforcing strict ascending order (`a < b`, `c > a`, `d > c`). This eliminated duplicate permutations and drastically reduced computation time without complex inequality checks.
- Task "Все вместе 2": Consolidated 6 distinct counting and summing conditions into a single, clean `while` loop without variable collision or redundant iterations.

Personal note: Passed the final exam under real-world constraints. Proved that structured algorithmic thinking holds up under pressure. Now switching to mandatory rest mode.
"""

  # Задача №1 - Ревью кода-7 🌶️
  # На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа или 0, если чётных цифр в записи нет. Программист торопился и написал программу неправильно.
  # Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
  # Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, использующую другой алгоритм решения.
  # код задача:
n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)

  # Исправленный:
n = int(input())
s = 0
while n != 0:
    digit = n % 10
    if digit % 2 == 0:
        s += digit
    n //= 10
if s > 0:
    print(s)
else:
    print(0)

  # Задача №2 - Ревью кода-8 🌶️
  # На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^12. Нужно написать программу, которая выводит на экран количество делящихся нацело на 
  # 4 чисел в исходной последовательности и максимальное делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет, на экран требуется вывести «NO» (без кавычек). Программист торопился и написал программу неправильно.
  # Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
  # код задачи:
n = 7
count = 0
maximum = 1000
for i in range(1, n + 1):
    x = int(input())
    if x // 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

  # исправленный:
count = 0
maximum = -1000000000001
for _ in range(8):
    x = int(input())
    if x % 4 == 0:
        count += 1
    if x % 4 == 0 and x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

  # Задача №3 - Ревью кода-9
  # На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^8. Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и максимальное нечётное число. Если нечётных чисел нет, требуется на экран вывести «NO» (без кавычек). Программист торопился и написал программу неправильно.
  # Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
  # код задачи:
n = 4
count = 0
maximum = 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = i
            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

  # исправленный:
count = 0
maximum = 0
for _ in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
            
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

  # Задача №4 - Звёздная рамка 🌟
  # На вход программе подаётся натуральное число n(3≤n≤19). Напишите программу, которая печатает звёздную рамку размерами n×19.
n = int(input())
print("*" * 19)
for i in range(n - 2):
    print("*", " " * 17, "*", sep = "")
print("*" * 19)

  # Задача №5 - Третья цифра 3️⃣
  # Дано натуральное число n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.
num = int(input())
n = len(str(num))
print((num // 10 ** (n - 3)) % 10)

  # Задача №6 - Все вместе 2
  # Дано натуральное число. Напишите программу, которая вычисляет:
  # количество цифр 3 в нём;
  # сколько раз в нём встречается последняя цифра;
  # количество чётных цифр;
  # сумму его цифр, больших пяти;
  # произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести её);
  # сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
num = int(input())
last_digit = num % 10
amt_3 = 0  # счетчик количества цифр 3
counter = 0  # счетчик с последней цифрой
counter1 = 0  # счетчик количества четных цифр
total = 0  # счетчик суммы цифр больше 5
total1 = 1  # счетчик произведение цифр, больших 7
counter2 = 0  # счетчик цифр 0 и 5
while num != 0:
    digit = num % 10
    if digit == 3:
        amt_3 += 1
    if digit == last_digit:
        counter += 1
    if digit % 2 == 0:
        counter1 += 1
    if digit > 5:
        total += digit
    if digit == 0 or digit == 5:
        counter2 += 1
    if digit > 7:
        total1 *= digit
    num //= 10
print(amt_3, counter, counter1, total, total1, counter2, sep = "\n")


  # Задача №7 - Числа Рамануджана 🌶️
  # Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было 1729
  # такое скучное и заурядное число. На что Рамануджан ответил: "Нет, нет! Это очень интересное число. Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами". Другими словами, 
  # 1729 =1^3+12^3=9^3+10^3
  # Напишите программу, которая находит аналогичные интересные числа. В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729.
  # Примечание. Используйте вложенный цикл.

  # переводим в уравнение a ** 3 + b ** 3 = c ** 3 + d ** 3
for a in range(1, 33):
    for b in range(a + 1, 33):       # Гарантирует, что a < b (исключаем 1,1 и перестановку 12,1)
        for c in range(a + 1, 33):   # Гарантирует, что вторая пара начинается с числа больше 'a'
            for d in range(c + 1, 33): # Гарантирует, что c < d
                if a**3 + b**3 == c**3 + d**3:
                    print(a**3 + b**3)
