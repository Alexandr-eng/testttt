
def generate_sequence(n):
    current_number = 1
    count = 0

    while count < n:
        # Генерируем текущее число current_number раз
        for _ in range(current_number):
            if count >= n:
                break
            yield current_number
            count += 1
        current_number += 1

# Ввод числа n
n = int(input("Введите количество элементов последовательности: "))

# Генерация и вывод последовательности
result = list(generate_sequence(n))
print("Последовательность:", " ".join(map(str, result)))