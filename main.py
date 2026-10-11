# Задание 3
print('--------Задание 3--------')

print('Hello, World!')

# Задание 4
print('--------Задание 4--------')

name = 'Ilya'
age = 18
height = 1.63
is_student = True
print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))
height = 1.65
name = 'Ilya L'
print(name, age, height, is_student)

# Задание 5
print('--------Задание 5--------')

name = input()
surename = input()

# age = input()
# print(type(age))

age = int(input())
height = float(input())
# print(name, surename, age, height)
# print(type(name), type(surename), type(age), type(height))

# Задание 6
print('--------Задание 6--------')

a = 15
b = 4
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)
print(2 + 3 * 4)
print((2 + 3) * 4)

# Задание 7
print('--------Задание 7--------')

x1, x2 = float(input()), float(input())
print(f'x1+x2={x1+x2}', f'x1-x2={x1-x2}', f'x1*x2={x1*x2}', f'x1/x2={x1/x2}', sep='\n')

# Задание 8
print('--------Задание 8--------')

# for i in range(1, 11):
#     print(i)
for i in range(10, 0, -1):
    print(i)

for i in range(0, 21, 2):
    print(i)
for i in range(0, 21, 4):
    print(i)

# Задание 9
print('--------Задание 9--------')

n = int(input())
s = 0
for i in range(n+1):
    s += i

print(s)

# Задание 10
print('--------Задание 10--------')

count = 10
while count > 0:
    print(count)
    count -= 1

print('Цикл завершён')

# Задание 11
print('--------Задание 11--------')

import math
radius = 3
c = 2 * math.pi * radius
s = math.pi * (radius**2)
x = math.sqrt(144)
print(x)

# Задание 12
print('--------Задание 12--------')

m = int(input())

if m > 0:
    print('Число положительное.')
elif m == 0:
    print('Число равно 0.')
else:
    print('Число отрицательное.')

if m % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')

# Задание 13
print('--------Задание 13--------')

age = int(input())
has_access = input()=='True'

if age >= 18 and has_access:
    print('Доступ разрешён')
else:
    print('Доступ запрещён')

# Задание 14
print('--------Задание 14--------')

n = int(input())
s = 0
for i in range(n):
    x = float(input())
    s += x
print(s, s/n)
