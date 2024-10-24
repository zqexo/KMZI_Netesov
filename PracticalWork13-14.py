import random
from sympy import gcd, mod_inverse, isprime, primerange


# gcd - Расширенный алгоритм Евклида.
# mod_inverse - Вычисляет мультипликативную обратную величину числа по модулю.
# isprime - Проверяет, является ли число простым.
# primerange - генерирует все простые числа в заданном диапазоне.


# Генерация простого числа p из таблицы простых чисел
def generate_prime(min_val=1000, max_val=10000):
    primes = list(primerange(min_val, max_val))
    return random.choice(primes)


# Генерация пары ключей (секретного и публичного) для участника
def generate_keys(p):
    while True:
        c = random.randint(2, p - 2)
        if isprime(c) and (gcd(c, p - 1) == 1):
            d = mod_inverse(c, p - 1)
            return c, d


# Преобразование сообщения в числовой код
def text_to_number(message):
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = []
    for i in range(0, len(message), 2):
        pair = message[i:i + 2]
        code = ''.join([f'{alphabet.index(ch) + 1:02}' for ch in pair])
        result.append(int('1' + code))  # Добавляем фиксированную цифру 1
    return result


# Обратное преобразование числового кода в текст
def number_to_text(numbers):
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = []

    for number in numbers:
        number_str = str(number)  # Преобразуем число в строку
        # Убираем фиксированное значение (если оно добавляется)
        number_str = number_str[1:]  # Убираем фиксированное значение 1

        if len(number_str) == 4:  # Должны быть две двузначные части
            try:
                # Извлекаем первые и вторые две цифры и конвертируем их в индексы
                first_index = int(number_str[:2]) - 1  # Первая буква
                second_index = int(number_str[2:]) - 1  # Вторая буква
                result.append(alphabet[first_index] + alphabet[second_index])
            except (ValueError, IndexError) as e:
                print(f"Ошибка при обработке числа: {number_str}, ошибка: {e}")
                result.append("??")  # Пометка о некорректных данных
        if len(number_str) == 2:
            try:
                # Извлекаем первую цифру и конвертируем ее в индекс
                index = int(number_str) - 1
                result.append(alphabet[index])
            except (ValueError, IndexError) as e:
                print(f"Ошибка при обработке числа: {number_str}, ошибка: {e}")
                result.append("?")  # Пометка о некорректных данных

        else:
            print(f"Неверный формат числа: {number_str}")
            result.append("??")

    return ''.join(result)


# Шифрование и расшифрование сообщения
def encrypt_decrypt(m, key, p):
    return pow(m, key, p)


# Основная функция
def shamir_cipher():
    # Заданные параметры
    p = 4871
    c_A = 1399
    d_A = 919
    c_B = 2999
    d_B = 4149
    message = 'БА'  # Сообщение
    print(f"Сообщение: {message}")

    # Преобразование текста в числовую форму
    numeric_message = [int('1' + str(ord(char) - ord('А') + 1).zfill(2)) for char in message]
    print(f"Числовая форма сообщения: {numeric_message}")

    # Шифрование участником A
    encrypted_A = [(pow(m, c_A, p)) for m in numeric_message]
    print(f"После шифрования участником A: {encrypted_A}")

    # Шифрование участником B
    encrypted_B = [(pow(m, c_B, p)) for m in encrypted_A]
    print(f"После шифрования участником B: {encrypted_B}")

    # Расшифрование участником B
    decrypted_by_B = [(pow(m, d_B, p)) for m in encrypted_B]
    print(f"После расшифрования участником B: {decrypted_by_B}")

    # Расшифрование участником A
    decrypted_by_A = [(pow(m, d_A, p)) for m in decrypted_by_B]
    print(f"После расшифрования участником A: {decrypted_by_A}")

    # Преобразование чисел обратно в текст
    decrypted_message = number_to_text(decrypted_by_A)
    print(f"Расшифрованное сообщение: {decrypted_message}")


# Запуск алгоритма
shamir_cipher()
