import random  # Импортируем модуль для генерации случайных чисел
from sympy import isprime  # Импортируем функцию для проверки простоты числа


def generate_large_prime(minimum=10 ** 2):
    """Генерирует большое простое число больше заданного минимального значения."""
    while True:
        num = random.randint(minimum, minimum * 10)  # Генерируем случайное число в диапазоне
        if isprime(num):  # Проверяем, является ли число простым
            return num  # Если да, возвращаем его


def generate_parameters():
    """Генерирует параметры p и g для системы Диффи-Хеллмана."""
    p = generate_large_prime()  # Генерируем большое простое число p
    # Выбираем g, которое должно быть меньше p и удовлетворять условиям
    g = random.randint(2, p - 1)  # Генерируем случайное число g
    return p, g  # Возвращаем параметры p и g


def generate_secret_key():
    """Генерирует случайный секретный ключ."""
    return random.randint(1, 100)  # Генерируем случайное число в диапазоне от 1 до 100


def calculate_public_key(g, secret_key, p):
    """Вычисляет открытый ключ на основе секретного ключа."""
    return pow(g, secret_key, p)  # Возвращаем g^secret_key mod p


def calculate_shared_secret(public_key, secret_key, p):
    """Вычисляет общий секретный ключ для шифрования."""
    return pow(public_key, secret_key, p)  # Возвращаем public_key^secret_key mod p


def caesar_cipher(text, shift):
    """Шифрует текст с помощью шифра Цезаря."""
    encrypted_text = ""  # Инициализируем пустую строку для зашифрованного текста
    for char in text:  # Проходим по каждому символу в тексте
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift_base = 65 if char.isupper() else 97  # Определяем базу для больших и маленьких букв
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)  # Шифруем букву
        else:
            encrypted_text += char  # Оставляем символ без изменений
    return encrypted_text  # Возвращаем зашифрованный текст


# Главная функция для демонстрации работы системы Диффи-Хеллмана
def main():
    # Генерируем параметры системы
    p, g = generate_parameters()
    print(f"Параметры системы: p = {p}, g = {g}")  # Выводим параметры p и g

    # Участники выбирают секретные ключи
    secret_key_a = generate_secret_key()
    secret_key_b = generate_secret_key()
    print(f"Секретные ключи: A = {secret_key_a}, B = {secret_key_b}")  # Выводим секретные ключи

    # Участники вычисляют открытые ключи
    public_key_a = calculate_public_key(g, secret_key_a, p)
    public_key_b = calculate_public_key(g, secret_key_b, p)
    print(f"Открытые ключи: A = {public_key_a}, B = {public_key_b}")  # Выводим открытые ключи

    # Участники вычисляют общий секретный ключ
    shared_secret_a = calculate_shared_secret(public_key_b, secret_key_a, p)
    shared_secret_b = calculate_shared_secret(public_key_a, secret_key_b, p)
    print(f"Общий секретный ключ: A = {shared_secret_a}, B = {shared_secret_b}")  # Проверяем, совпадают ли ключи

    # Проверяем совпадение общего секретного ключа
    assert shared_secret_a == shared_secret_b, "Общие ключи не совпадают!"

    # Шифрование и дешифрование текста
    message = "Hello World"  # Исходное сообщение
    print(f"Исходное сообщение: {message}")  # Выводим исходное сообщение
    encrypted_message = caesar_cipher(message, shared_secret_a)  # Шифруем сообщение
    print(f"Зашифрованное сообщение: {encrypted_message}")  # Выводим зашифрованное сообщение
    decrypted_message = caesar_cipher(encrypted_message, -shared_secret_a)  # Дешифруем сообщение
    print(f"Расшифрованное сообщение: {decrypted_message}")  # Выводим расшифрованное сообщение


if __name__ == "__main__":  # Проверяем, запущен ли скрипт напрямую
    main()  # Вызываем главную функцию
