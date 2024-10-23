# Магический квадрат 4x4
# Вариант 20(мой вариант) % 12(всего вариантов) = 8
magic_square = [[1, 12, 13, 8], [15, 6, 3, 10], [4, 9, 16, 5], [14, 7, 2, 11]]


def encrypt_magic_square(text):
    # Удаляем пробелы и переводим текст в верхний регистр для единообразия
    text = text.replace(" ", "").upper()
    n = len(magic_square)  # Размер магического квадрата (4 для 4x4)
    matrix = [""] * (n * n)  # Создаем пустой список для зашифрованного сообщения

    # Записываем текст в магический квадрат по номерам ячеек
    index = 0  # Индекс для символов текста
    for i in range(n):
        for j in range(n):
            if index < len(text):  # Если есть еще символы в тексте
                matrix[magic_square[i][j] - 1] = text[
                    index
                ]  # Вписываем символ в соответствующую ячейку
                index += 1
            else:
                matrix[magic_square[i][j] - 1] = (
                    " "  # Заполняем пробелами, если текст короче квадрата
                )

    # Собираем зашифрованное сообщение из заполненной матрицы по строкам
    encrypted_text = "".join(matrix)
    return encrypted_text


def decrypt_magic_square(encrypted_text):
    n = len(magic_square)  # Размер магического квадрата (4 для 4x4)
    matrix = [""] * (n * n)  # Создаем пустой список для расшифрованного сообщения

    # Заполняем матрицу зашифрованным текстом по строкам
    index = 0
    for i in range(n * n):
        if index < len(encrypted_text):  # Если есть еще символы в зашифрованном тексте
            matrix[i] = encrypted_text[
                index
            ]  # Заполняем матрицу символами зашифрованного текста
            index += 1

    # Собираем исходное сообщение, читая матрицу по номерам ячеек магического квадрата
    decrypted_text = ""
    for i in range(n):
        for j in range(n):
            decrypted_text += matrix[
                magic_square[i][j] - 1
            ]  # Собираем символы по их номеру в магическом квадрате

    return decrypted_text


# Тестирование
message = "ТЕСТ ПРОЙДЕН"
# Шифруем сообщение с помощью магического квадрата
encrypted_message = encrypt_magic_square(message)
# print(f"Зашифрованное сообщение: {encrypted_message}")

# Расшифровываем сообщение обратно
decrypted_message = decrypt_magic_square(encrypted_message)
# print(f"Расшифрованное сообщение: {decrypted_message}")

# ________________________________________________________________


# Русский алфавит
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_size = len(alphabet)  # Количество символов в алфавите (33)


def generate_vigenere_square():
    # Генерация квадрата Виженера для русского алфавита
    vigenere_square = []
    for i in range(alphabet_size):
        # Создаем строку, которая начинается с текущей буквы и заканчивается оставшимися буквами
        row = alphabet[i:] + alphabet[:i]
        vigenere_square.append(row)  # Добавляем эту строку в квадрат Виженера
    return vigenere_square


# Генерируем квадрат Виженера
vigenere_square = generate_vigenere_square()


def encrypt_vigenere(text, key):
    # Удаляем пробелы и переводим текст и ключ в верхний регистр для единообразия
    text = text.replace(" ", "").upper()
    key = key.upper()
    encrypted_text = ""  # Переменная для хранения зашифрованного сообщения
    key_index = 0  # Индекс для перемещения по ключу

    for char in text:
        if char in alphabet:  # Проверяем, является ли символ буквой алфавита
            # Определяем индекс строки и столбца в квадрате Виженера
            row = alphabet.index(char)  # Индекс строки по символу текста
            col = alphabet.index(
                key[key_index % len(key)]
            )  # Индекс столбца по символу ключа
            encrypted_text += vigenere_square[row][
                col
            ]  # Добавляем зашифрованный символ в сообщение
            key_index += 1  # Переходим к следующему символу ключа
        else:
            encrypted_text += (
                char  # Добавляем символ без изменений, если это не буква алфавита
            )

    return encrypted_text


def decrypt_vigenere(encrypted_text, key):
    key = key.upper()  # Переводим ключ в верхний регистр
    decrypted_text = ""  # Переменная для хранения расшифрованного сообщения
    key_index = 0  # Индекс для перемещения по ключу

    for char in encrypted_text:
        if char in alphabet:  # Проверяем, является ли символ буквой алфавита
            # Определяем индекс столбца и строки в квадрате Виженера
            col = alphabet.index(
                key[key_index % len(key)]
            )  # Индекс столбца по символу ключа
            # Находим индекс строки, в которой находится зашифрованный символ
            row = next(i for i, row in enumerate(vigenere_square) if row[col] == char)
            decrypted_text += alphabet[
                row
            ]  # Добавляем расшифрованный символ в сообщение
            key_index += 1  # Переходим к следующему символу ключа
        else:
            decrypted_text += (
                char  # Добавляем символ без изменений, если это не буква алфавита
            )

    return decrypted_text


# Тестирование
message = "ЭТОТ ТЕКСТ ПРЕДНАЗНАЧЕН ДЛЯ ТЕСТИРОВАНИЯ СИСТЕМЫ ВИЖЕНЕРА"
key = "Ключ"  # Ключевое слово для шифрования и расшифрования
# Шифруем сообщение с помощью системы Виженера
encrypted_message = encrypt_vigenere(message, key)
print(f"Зашифрованное сообщение (Виженер): {encrypted_message}")

# Расшифровываем сообщение обратно
decrypted_message = decrypt_vigenere(encrypted_message, key)
print(f"Расшифрованное сообщение (Виженер): {decrypted_message}")

print("\nПолучившийся квадрат Виженера:")


# Функция для печати квадрата Виженера
def print_vigenere_square(vigenere_square):
    # Печатаем заголовок с алфавитом
    print("  ", end="")  # Выравниваем первую строку
    for letter in alphabet:
        print(f"{letter} ", end="")  # Печать букв алфавита
    print()  # Перевод строки

    # Печать каждой строки квадрата Виженера с заголовком
    for i, row in enumerate(vigenere_square):
        print(f"{alphabet[i]} ", end="")  # Печать заголовка строки
        for letter in row:
            print(f"{letter} ", end="")  # Печать символов строки с пробелами
        print()  # Перевод строки


print_vigenere_square(vigenere_square)
