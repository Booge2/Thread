import threading
import multiprocessing as mp
import json
import random
import time


# def find_max(numbers):
#     max_value = max(numbers)
#     print("Максимум у списку:", max_value)
#
#
# def find_min(numbers):
#     min_value = min(numbers)
#     print("Мінімум у списку:", min_value)
#
#
# def main():
#     numbers = []
#     n = int(input("Введіть кількість чисел у списку: "))
#     print("Введіть числа:")
#     for _ in range(n):
#         num = int(input())
#         numbers.append(num)
#
#     t1 = threading.Thread(target=find_max, args=(numbers,))
#     t2 = threading.Thread(target=find_min, args=(numbers,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     main()
#
#
# # Завдання 2
#
# def find_sum(numbers):
#     total = sum(numbers)
#     print("Сума елементів у списку:", total)
#
#
# def find_average(numbers):
#     if len(numbers) == 0:
#         print("Список порожній, немає середнього арифметичного")
#         return
#     average = sum(numbers) / len(numbers)
#     print("Середнє арифметичне елементів у списку:", average)
#
#
# def main():
#     numbers = []
#     n = int(input("Введіть кількість чисел у списку: "))
#     print("Введіть числа:")
#     for _ in range(n):
#         num = int(input())
#         numbers.append(num)
#
#     t1 = threading.Thread(target=find_sum, args=(numbers,))
#     t2 = threading.Thread(target=find_average, args=(numbers,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     main()
#
#
# # Завдання 3
#
#
# def process_even_numbers(filename):
#     with open(filename, 'r') as file:
#         numbers = json.load(file)
#
#     even_numbers = [num for num in numbers if num % 2 == 0]
#     even_filename = 'even_numbers.txt'
#
#     with open(even_filename, 'w') as even_file:
#         for num in even_numbers:
#             even_file.write(str(num) + '\n')
#
#     print("Кількість парних чисел:", len(even_numbers))
#
#
# def process_odd_numbers(filename):
#     with open(filename, 'r') as file:
#         numbers = json.load(file)
#
#     odd_numbers = [num for num in numbers if num % 2 != 0]
#     odd_filename = 'odd_numbers.txt'
#
#     with open(odd_filename, 'w') as odd_file:
#         for num in odd_numbers:
#             odd_file.write(str(num) + '\n')
#
#     print("Кількість непарних чисел:", len(odd_numbers))
#
#
# def main():
#     numbers = input("Введіть числа, розділені комою: ")
#     numbers_list = [int(num.strip()) for num in numbers.split(',')]
#
#     filename = 'numbers.json'
#     with open(filename, 'w') as file:
#         json.dump(numbers_list, file)
#
#     process1 = mp.Process(target=process_even_numbers, args=(filename,))
#     process2 = mp.Process(target=process_odd_numbers, args=(filename,))
#
#     process1.start()
#     process2.start()
#
#     process1.join()
#     process2.join()
#
#
# if __name__ == "__main__":
#     main()
# # Завдання 4
# def producer(queue, data):
#     for item in data:
#         queue.put(item)
#         print(f"Producer put {item} into the queue")
#         time.sleep(random.randint(1, 3))
#
#
# def consumer(queue):
#     while True:
#         item = queue.get()
#         print(f"Consumer got {item} from the queue")
#         time.sleep(random.randint(1, 3))
#         queue.task_done()
#
#
# def main():
#     queue = mp.JoinableQueue()
#
#     producer_process = mp.Process(target=producer, args=(queue, [1, 2, 3, 4, 5]))
#     consumer_process = mp.Process(target=consumer, args=(queue,))
#
#     producer_process.start()
#     consumer_process.start()
#
#     producer_process.join()
#     queue.join()
#
#     consumer_process.terminate()
#
#
# if __name__ == "__main__":
#     main()
# # Завдання 5

def process_data(data_chunk):
    processed_data = sorted(data_chunk)
    return processed_data

def main():
    array_size = 10000
    big_data = [random.randint(1, 1000) for _ in range(array_size)]

    num_processes = mp.cpu_count()
    chunk_size = len(big_data) // num_processes
    data_chunks = [big_data[i:i + chunk_size] for i in range(0, len(big_data), chunk_size)]

    with mp.Pool(processes=num_processes) as pool:
        processed_results = pool.map(process_data, data_chunks)

    final_result = []
    for result in processed_results:
        final_result.extend(result)

    print(f"Sorted array: {final_result}")

if __name__ == "__main__":
    main()
