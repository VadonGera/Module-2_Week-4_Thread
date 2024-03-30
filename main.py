import threading


# Функция, которую выполняем в отдельном потоке
def square(numb, i):
    numbers[i] = numb ** 2


# Функция для расчета квадратов чисел списка, которая использует многопоточность.
def compute_squares(numbers):
    # Запуск потоков на каждый элемент списка.
    threads = [threading.Thread(target=square, args=(numbers[i], i)) for i in range(0, len(numbers))]
    for thread in threads:
        thread.start()

    # Ждем завершения потоков
    for thread in threads:
        thread.join()

    # Возвращаем измененный список.
    return numbers


if __name__ == "__main__":
    # Список чисел, которые возводим в квадрат
    numbers = [95555555555, 1, 2, 3, 10, 100, 200, 300, 500, 200]

    print(compute_squares(numbers))
