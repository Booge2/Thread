import threading
import multiprocessing as mp
import json


def find_max(numbers):
    max_value = max(numbers)
    print("Максимум у списку:", max_value)


def find_min(numbers):
    min_value = min(numbers)
    print("Мінімум у списку:", min_value)


def main():
    numbers = []
    n = int(input("Введіть кількість чисел у списку: "))
    print("Введіть числа:")
    for _ in range(n):
        num = int(input())
        numbers.append(num)

    t1 = threading.Thread(target=find_max, args=(numbers,))
    t2 = threading.Thread(target=find_min, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()


# Завдання 2

def find_sum(numbers):
    total = sum(numbers)
    print("Сума елементів у списку:", total)


def find_average(numbers):
    if len(numbers) == 0:
        print("Список порожній, немає середнього арифметичного")
        return
    average = sum(numbers) / len(numbers)
    print("Середнє арифметичне елементів у списку:", average)


def main():
    numbers = []
    n = int(input("Введіть кількість чисел у списку: "))
    print("Введіть числа:")
    for _ in range(n):
        num = int(input())
        numbers.append(num)

    t1 = threading.Thread(target=find_sum, args=(numbers,))
    t2 = threading.Thread(target=find_average, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()


# Завдання 3


def process_even_numbers(filename):
    with open(filename, 'r') as file:
        numbers = json.load(file)

    even_numbers = [num for num in numbers if num % 2 == 0]
    even_filename = 'even_numbers.txt'

    with open(even_filename, 'w') as even_file:
        for num in even_numbers:
            even_file.write(str(num) + '\n')

    print("Кількість парних чисел:", len(even_numbers))


def process_odd_numbers(filename):
    with open(filename, 'r') as file:
        numbers = json.load(file)

    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_filename = 'odd_numbers.txt'

    with open(odd_filename, 'w') as odd_file:
        for num in odd_numbers:
            odd_file.write(str(num) + '\n')

    print("Кількість непарних чисел:", len(odd_numbers))


def main():
    numbers = input("Введіть числа, розділені комою: ")
    numbers_list = [int(num.strip()) for num in numbers.split(',')]

    filename = 'numbers.json'
    with open(filename, 'w') as file:
        json.dump(numbers_list, file)

    process1 = mp.Process(target=process_even_numbers, args=(filename,))
    process2 = mp.Process(target=process_odd_numbers, args=(filename,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == "__main__":
    main()
