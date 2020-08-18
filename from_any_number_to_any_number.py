##############################English description################################
# Doesn't use internal int function to convert a number to the 10-digit number system, uses its own algorithm.
# Not limited to 36-digit numeral system, will go further down the symbol table.
# No protection against incorrect data entry, just a demonstration of the algorithm.
# Doesn't do unnecessary conversions when they are not needed.
# Actually it is a calculator for converting numbers from any number system to any other.

###############################Описание на русском################################
# Не использует внутренню функцию int для приведения числа к 10-чной системе счисления, используется свой алгоритм.
# Не ограничен 36-чной системой счисления, пойдет дальше по таблице символов.
# Нет защиты от ввода неправильных данных, только демонстрация алгоритма.
# Не делает лишниие конвертации, когда они не нужны.
# Фактически является калькулятором для перевод чисел из любой системы счисления в любую другую.

def transition(x, base, digit = ""):
    if base != 10:
        while x>0:
            if x%base>9: digit = chr(x%base+87).upper() + digit
            else: digit = str(x%base) + digit
            x //= base
        print(f"Возвращаем готовый результат = {digit}")
    else: print(f"Мгновенный возрат, число на входе сразу десятичное = {x}")
	
def any_to_10(source_in, n, formula=0):
    if n == 10: return int(source_in)
    source = list(source_in)
    for i in range(len(source)):
        if n != 10 and source[i] != '0' and source[i].isalpha():
            formula += (ord(source[i].lower())-87) * (n**(len(source)-(i+1)))
        elif source[i] != '0': formula += int(source[i]) * (n**(len(source)-(i+1)))
    return formula

print("Введите n-ичность счисления для вашего числа: ", end="")
r = int(input())
print("Введите соответствующее число для конвертации: ", end="")
x = any_to_10(input(), r)
print("Введите в какую систему счисления перевести ваше число: ",end="")
base = int(input())

transition(x, base)