import time
from multiprocessing import Pool, cpu_count


def factorize_number(number):
    return [i for i in range(1, number + 1) if number % i == 0]


def run_sync(*numbers):
    start_time = time.time()
    result = [factorize_number(num) for num in numbers]
    end_time = time.time()
    print(f"Синхронна версія: {end_time - start_time:.2f} секунд")
    return result


def run_parallel(*numbers):
    start_time = time.time()
    with Pool(cpu_count()) as p:
        result = p.map(factorize_number, numbers)
    end_time = time.time()
    print(f"Паралельна версія: {end_time - start_time:.2f} секунд")
    return result


if __name__ == "__main__":
    print(f"Кількість ядер процесора: {cpu_count()}")

    sync_result = run_sync(128, 255, 99999, 10651060)
    parallel_result = run_parallel(128, 255, 99999, 10651060)

    a, b, c, d = sync_result

    print(a)
    print(b)
    print(c)
    print(d)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    print("Всі тести пройдені успішно!")
