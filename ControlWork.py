import random  # Импортируем модуль random для генерации случайных чисел


# 1. Возведение в степень по модулю
def modular_exponentiation(base, exponent, modulus):
    result = 1  # Инициализируем результат
    base = base % modulus  # Применяем модуль к основанию
    while exponent > 0:  # Пока показатель больше 0
        if (exponent % 2) == 1:  # Если показатель нечетный
            result = (result * base) % modulus  # Умножаем на основание
        exponent = exponent >> 1  # Делим показатель на 2
        base = (base * base) % modulus  # Возводим основание в квадрат
    return result  # Возвращаем результат


# 2. Вычисление наибольшего общего делителя (gcd)
def gcd(a, b):
    while b != 0:  # Пока b не равно 0
        a, b = b, a % b  # Применяем алгоритм Евклида
    return a  # Возвращаем наибольший общий делитель


# 3. Вычисление инверсии (x^(-1) mod m)
def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1  # Инициализируем m и x
    if m == 1:
        return 0  # Если модуль равен 1, инверсии нет
    while a > 1:  # Пока a больше 1
        q = a // m  # Получаем частное
        m, a = a % m, m  # Обновляем значения
        x0, x1 = x1 - q * x0, x0  # Обновляем значения x
    if x1 < 0:  # Если x1 отрицательное
        x1 += m0  # Приводим его к положительному
    return x1  # Возвращаем инверсию


# 4. Система Диффи–Хеллмана
def diffie_hellman(p, g):
    a = random.randint(1, p - 1)  # Генерируем секретный ключ A
    b = random.randint(1, p - 1)  # Генерируем секретный ключ B

    A = modular_exponentiation(g, a, p)  # Вычисляем открытый ключ A
    B = modular_exponentiation(g, b, p)  # Вычисляем открытый ключ B

    # Общий секрет
    shared_secret_A = modular_exponentiation(B, a, p)  # Секрет для A
    shared_secret_B = modular_exponentiation(A, b, p)  # Секрет для B

    return shared_secret_A, shared_secret_B  # Возвращаем общий секрет


# 5. Шифр Шамира
def shamir_encryption(message, p):
    k = random.randint(1, p - 2)  # Генерируем секретный ключ
    encrypted_message = (message * modular_exponentiation(g1, k, p)) % p  # Шифруем сообщение
    return encrypted_message  # Возвращаем зашифрованное сообщение


# 6. Шифр Эль-Гамаля
def elgamal_encryption(message, p, g):
    k = random.randint(1, p - 2)  # Генерируем секретный ключ
    c1 = modular_exponentiation(g, k, p)  # Вычисляем первую часть шифротекста
    c2 = (message * modular_exponentiation(g, k, p)) % p  # Вычисляем вторую часть шифротекста
    return c1, c2  # Возвращаем зашифрованное сообщение


# 7. RSA
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1  # Если a равно 0, возвращаем b
    gcd, x1, y1 = gcd_extended(b % a, a)  # Рекурсивный вызов для вычисления GCD
    x = y1 - (b // a) * x1  # Обновляем x
    y = x1  # Обновляем y
    return gcd, x, y  # Возвращаем GCD и коэффициенты


def rsa_encrypt(message, e, n):
    return modular_exponentiation(message, e, n)  # Шифруем сообщение


def rsa_decrypt(ciphertext, d, n):
    return modular_exponentiation(ciphertext, d, n)  # Дешифруем сообщение


# ВАРИАНТ 20
# Указанные параметры
p1 = 18911
g1 = 2
p2 = 18911
p3 = 18911
g3 = 2
PA = 131
QA = 241
PB = 479
QB = 617
dA = 3
dB = 3

# Пример использования системы Диффи–Хеллмана
print("\nПример использования системы Диффи–Хеллмана")
shared_secret = diffie_hellman(p1, g1)
print(f"Общий секрет: {shared_secret}")

# Пример шифрования с помощью Шамира
print("\nПример шифрования с помощью Шамира")
message_shamir = 42  # Пример сообщения
encrypted_shamir = shamir_encryption(message_shamir, p2)
print(f"Зашифрованное сообщение Шамира: {encrypted_shamir}")

# Пример шифрования с помощью Эль-Гамаля
print("\nПример шифрования с помощью Эль-Гамаля")
message_elgamal = 42  # Пример сообщения
ciphertext_elgamal = elgamal_encryption(message_elgamal, p3, g3)
print(f"Зашифрованное сообщение Эль-Гамаля: {ciphertext_elgamal}")


# Пример использования RSA
print("\nПример использования RSA")
nA = PA * QA  # Общий модуль для A
nB = PB * QB  # Общий модуль для B

# Шифрование и дешифрование
message_rsa = 42  # Пример сообщения
ciphertext_A = rsa_encrypt(message_rsa, dA, nA)  # Шифруем сообщение для A
decrypted_message_A = rsa_decrypt(ciphertext_A, dA, nA)  # Дешифруем сообщение для A

ciphertext_B = rsa_encrypt(message_rsa, dB, nB)  # Шифруем сообщение для B
decrypted_message_B = rsa_decrypt(ciphertext_B, dB, nB)  # Дешифруем сообщение для B

print(f"Зашифрованное сообщение RSA (A): {ciphertext_A}, Дешифрованное сообщение: {decrypted_message_A}")
print(f"Зашифрованное сообщение RSA (B): {ciphertext_B}, Дешифрованное сообщение: {decrypted_message_B}")
