# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    ...
    s = input()
    first, second = s.split(',', 1)
    print(len(first) > len(second))
    print(first == second)
    print(second in first)
# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    ...
    s = input()
    print(s.strip())
    print(len(s))
    print(s.count('a'))
    print(s.replace('a', '@'))
    print(s.istitle() or (len(s) > 0 and s[0].isupper()))
# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    ...
    s = input()
    print(s[1:-1])
    print(s[::2])
    print(s.lower()[::-1])
# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    ...
    data = input()
    numbers = list(map(int, data.split()))
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    sum_numbers = sum(numbers)
    print(sum_numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    print(min_number, max_number)

# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    ...
    s = input()
    result = (s.lower() == s.lower()[::-1]) and (' ' not in s)
    print(result)
# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    ...
    num = int(input())
    hex_str = hex(num)[2:]
    print(hex_str)
    print(len(hex_str))
    print('a' in hex_str)
# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    ...
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    n = int(input())
    print(months[n - 1])