import random
from sympy import isprime  # Проверяет простое число


# Функция для генерации большого простого числа p
def generate_large_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p


# Функция для получения первообразного корня
def find_primitive_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1) // factor, p) != 1 for factor in set(factors(p - 1))):
            return g
    return None


# Факторизация числа
def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result


# Генерация открытого и секретного ключа
def generate_keys(p, g):
    c = random.randint(1, p - 2)
    d = pow(g, c, p)
    return c, d


# Шифрование
def encrypt(m, d_B, p, g):
    k = random.randint(1, p - 2)
    r = pow(g, k, p)
    e = (m * pow(d_B, k, p)) % p
    return r, e


# Расшифровка
def decrypt(r, e, c_B, p):
    s = pow(r, p - 1 - c_B, p)
    m = (e * s) % p
    return m


# Расшифровка в виде текста
def number_to_letter(num):
    # Убираем первую единицу из числа и преобразуем его в строку
    str_num = str(num)[1:]

    # Разбиваем строку на двухзначные числа
    pairs = [str_num[i:i + 2] for i in range(0, len(str_num), 2)]

    # Создаем алфавит
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    # Находим соответствующие буквы
    letters = []
    for pair in pairs:
        if pair.isdigit():  # Проверяем, что это число
            index = int(pair) - 1  # Порядковый номер в алфавите (индексирование с 0)
            if 0 <= index < len(alphabet):
                letters.append(alphabet[index])

    return ''.join(letters)


# Основной код
if __name__ == "__main__":
    # Параметры
    p = 30803  # большое простое число
    g = 2  # первообразный корень

    # Генерация ключей для абонента B
    c_B, d_B = generate_keys(p, g)

    # Публикация параметров
    print(f"Параметры: p = {p}, g = {g}, открытый ключ d_B = {d_B}")

    # Пример передачи сообщения
    message = "БА"  # Исходное сообщение
    print(f"Исходное сообщение: {message}")
    m = 10201  # Представление сообщения в числовом виде

    # Шифрование
    r, e = encrypt(m, d_B, p, g)
    print(f"Зашифрованное сообщение: r = {r}, e = {e}")

    # Расшифровка
    m_prime = decrypt(r, e, c_B, p)
    print(f"Расшифрованное сообщение: m' = {m_prime}")
    print(f"Текст расшифрованного сообщения: {number_to_letter(m_prime)}")
