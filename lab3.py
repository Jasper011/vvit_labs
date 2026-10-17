import math


def greet(name):
    print(f"Здравствуйте, {name}!")


def square(number):
    return number ** 2


def max_of_two(a, b):
    if a > b:
        return a
    return b

print(greet('Ilya'))
print(greet('Ivan'))

print(square(2))
print(square(4))

print(max_of_two(10, 11))
print(max_of_two(9999, 1))

print("=" * 30, "Задание 2", "=" * 30)

def calculate_rectangle(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def describe_rectangle(width, height, unit="см"):
    print(f"Прямоугольник {width} x {height} {unit}: "
          f"площадь = {calculate_rectangle(width, height)} {unit}^2, "
          f"периметр = {calculate_perimeter(width, height)} {unit}")

print(calculate_rectangle(6, 4))
print(calculate_perimeter(6, 4))

describe_rectangle(6, 4)
describe_rectangle(6, 4, unit="дюйм")
describe_rectangle(height=2, width=9, unit="м")

print("=" * 30, "Задание 3", "=" * 30)

value = 10


def show_scope():
    value = 20
    print(value)

show_scope()
print(value)

print("=" * 30, "Задание 4", "=" * 30)

numbers = [42, 17, 93, 8, 56, 71, 25, 64, 39, 12]
print(numbers)
print(numbers[0])
print(numbers[2])
print(numbers[-1])

numbers[1] = 100
print(numbers)

numbers.append(77)
print(numbers)

numbers.remove(93)
print(numbers)

removed = numbers.pop()
print(removed)
print(numbers)
print(len(numbers))

print("=" * 30, "Задание 5", "=" * 30)

values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(values)
print(values[:3])
print(values[-3:])
print(values[2:7])
print(values[::2])
print(values[::-1])

print("=" * 30, "Задание 6", "=" * 30)

measurements = (12.5, 48.0, 7.25, 33.1, 91.4, 5.6, 60.0, 22.8)
print(measurements)
print(measurements[0])
print(measurements[-1])
print(measurements[1:5])

try:
    measurements[0] = 99
except TypeError as error:
    print("TypeError:", error)

first, second = measurements[:2]
print(first, second)

as_list = list(measurements)
print(as_list)
as_list[0] = 99
print(as_list)
back_to_tuple = tuple(as_list)
print(back_to_tuple)

print("=" * 30, "Задание 7", "=" * 30)

numbers = [42, 17, 93, 8, 56, 71, 25, 64, 39, 12]
print(numbers)
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))

copy_sorted = sorted(numbers)
print(copy_sorted)

numbers.sort()
print(numbers)

print("=" * 30, "Задание 8", "=" * 30)

def my_sum(numbers):
    total = 0
    for value in numbers:
        total += value
    return total


def my_min(numbers):
    minimum = math.inf
    for value in numbers:
        if value < minimum:
            minimum = value
    return minimum


def my_max(numbers):
    maximum = -math.inf
    for value in numbers:
        if value > maximum:
            maximum = value
    return maximum


def calculate_average(numbers):
    return my_sum(numbers) / len(numbers)


def find_minimum(numbers):
    return my_min(numbers)


def find_maximum(numbers):
    return my_max(numbers)

numbers = [42, 17, 93, 8, 56, 71, 25, 64, 39, 12]
print(numbers)
print(my_sum(numbers), sum(numbers))
print(my_min(numbers), min(numbers))
print(my_max(numbers), max(numbers))

print("=" * 30, "Задание 9", "=" * 30)

def linear_search(sequence, target):
    for index, value in enumerate(sequence):
        if value == target:
            return index
    return -1

numbers = [42, 17, 93, 8, 56, 71, 25, 64, 39, 12]
print(numbers)
print(linear_search(numbers, 56))
print(linear_search(numbers, 100))

print("=" * 30, "Задание 10", "=" * 30)

def analyze(numbers):
    return (my_min(numbers), my_max(numbers), calculate_average(numbers))

numbers = [42, 17, 93, 8, 56, 71, 25, 64, 39, 12]
result = analyze(numbers)
print(result)
minimum, maximum, average = result
print(minimum, maximum, average)

print("=" * 30, "Задание 11", "=" * 30)

def sort_demo(values):
    normal = sorted(values)
    by_abs = sorted(values, key=lambda x: abs(x))
    return normal, by_abs

values = [-15, 3, -7, 22, -1, 10, -30, 8]
print(values)
normal, by_abs = sort_demo(values)
print(normal)
print(by_abs)

print("=" * 30, "Задание 12", "=" * 30)

def analyze_measurements(measurements):
    return (find_minimum(measurements),
            find_maximum(measurements),
            calculate_average(measurements))


def count_above_average(measurements):
    average = calculate_average(measurements)
    count = 0
    for value in measurements:
        if value > average:
            count += 1
    return count

target = 51.7
measurements = [23.4, 45.1, 12.8, 67.9, 34.2, 89.5, 5.3, 51.7, 78.0, 40.6]
print(measurements)

minimum, maximum, average = analyze_measurements(measurements)
print(len(measurements))
print(minimum)
print(maximum)
print(round(average, 2))
print(count_above_average(measurements))

index = linear_search(measurements, target)
print(index)

missing = 99.9
index2 = linear_search(measurements, missing)
print(index2)
