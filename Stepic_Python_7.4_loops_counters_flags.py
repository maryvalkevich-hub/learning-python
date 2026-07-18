"""
Stepik: Python Programming
Topic: Loop 'for' — Counters, Totals, Flags, and Fibonacci
Date: 17-18 July 2026
Status: Completed ✅

Tasks solved: 11 (№1-11)
Topics covered:
- Counter, total, smallest/largest patterns
- Augmented assignment operators (+=, *=)
- Signal flags (boolean logic in loops)
- Variable swapping (a, b = b, a+b)
- Fibonacci sequence generation

Notable challenges:
- Task #10: Finding the two largest numbers (required careful initialization)
- Task #4: Mathematical optimization (squares ending in 2, 5, 8)
- Task #11: Fibonacci via tuple unpacking (elegant solution!)

Personal note: Solved these after a sleepless night. Python logic is a great distraction!
"""

  # Задача №11 - Последовательность Фибоначчи 🌶️.Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
  # Примечание. Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих.
n = int(input())
a = 0
b = 1
for _ in range(0, n):
     a, b = b, a + b
     print(a, end = " ")
          

  # Задача №10 - Наибольшие числа 🌶️.На вход программе подаются натуральное число n(n≥2), а затем n различных натуральных чисел последовательности, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
n = int(input())
largest = -1
largest2 = -1
for _ in range(n):
    num = int(input())
    if num > largest:
        largest2 = largest
        largest = num
    elif largest2 < num < largest:
        largest2 = num
 
print(largest, largest2, sep = "\n")

  # Задача №9 - Знакочередующаяся сумма. На вход программе подаётся натуральное число n. Напишите программу вычисления знакочередующейся суммы:
  # 1−2+3−4+5−6+…+(−1)^n+1 ⋅n
n = int(input())
total = 0
for i in range(1, n + 1):
     if i % 2 != 0:
          total += i
     elif i % 2 == 0:
          total -= i
print(total)

  # Задача №8 - Only even numbers. Напишите программу, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое из них чётным или нет.
total = 1
for _ in range(10):
     num = int(input())
     if num % 2 != 0:
        total *= 0
if total == 1:
     print("YES")
elif total == 0:
     print("NO")

  # Вариант 2
flag = "YES"
for _ in range(10):
     num = int(input())
     if num % 2 != 0:
          flag = "NO"
print(flag)


  # Задача №7 - Сумма делителей. На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
  # Примечание 1. Сумма делителей числа – это сумма всех чисел, на которые данное число делится без остатка. Например, делители числа 12 – это числа 1,2,3,4,6,12. Их сумма равна 1+2+3+4+6+12=28
  # Примечание 2. Функция подсчёта суммы всех делителей числа является очень важной в теории чисел.
n = int(input())
total = 0
for i in range(1, n + 1):
     if n % i == 0:
          total += i
print(total)

  # Задача №6 - Без нулей 0️.Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
  # Примечание 1. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
  # Примечание 2. Отличные от нуля числа – те числа, которые не равны нулю.
total = 1
for _ in range(10):
     num = int(input())
     if num != 0:  # Так как отличные от нуля число - это не обязательно только положительные.
          total *= num
print(total)

  # Задача №5 - Факториал ❗ На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет n!.
  # Примечание. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть n!=1⋅2⋅3⋅…⋅n
n = int(input())
from math import factorial
print(factorial(n))

  # Задача №4 - Сумма чисел 2. На вход программе подаётся натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), квадрат которых оканчивается на 2, на 5 или на 8.
  # Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 0.
n = int(input())
total = 0
flag = False
from math import pow
for i in range(1, n + 1):
     if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:  # Так как не существует чисел, квадрат которых оканчивается на 2 и на 8, можно написать if pow(i, 2) % 10 == 5. Но я пошла путем, если бы я это не знала.
          flag = True
          total += i
if flag == True:
     print(total)
elif flag == False:
     print(0)


  # Задача №3 - Асимптотическое приближение 📉.На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет значение выражения:
  # (1/1 + 1/2 + 1/3 + ... + 1/n) - ln(n)
  # Примечание. Для вычисления натурального логарифма ln(n) воспользуйтесь функцией log(n), которая находится в модуле math.
n = int(input())
from math import log
total = 0
for i in range(1, n + 1):
        total += 1 / i
b = total - log(n)
print(b)


  # Задача №2 - Сумма чисел. На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введённых чисел (не включая само число n).  
num = int(input())
total = 0
for _ in range(num):
    a = int(input())
    total += a
print(total)

  # Задача №1 - Количество чисел. На вход программе подаются два целых числа a и b(a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b (включительно), куб которых оканчивается на 4 или 9.
  # Примечание. Куб числа a – это его третья степень (a^3).
a, b = int(input()), int(input())
from math import pow
counter = 0
for i in range(a, b + 1):
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
        counter = counter + 1

print(counter)
