import numpy as np


class HillCipher:
    def __init__(self, encryption_matrix, decryption_matrix, mod=26):
        # Инициализация объекта класса с матрицами шифрования и расшифрования
        # На английском языке (mod=26)
        self.encryption_matrix = np.array(encryption_matrix)  # Матрица для шифрования
        self.decryption_matrix = np.array(
            decryption_matrix
        )  # Матрица для расшифрования
        self.mod = mod  # Модуль, по которому будут выполняться все операции (по умолчанию 26 для английского алфавита)

    @staticmethod
    def _text_to_vector(text):
        """Преобразует текст в числовой вектор, где 'A' = 0, 'B' = 1, ..., 'Z' = 25"""
        return [
            ord(char) - ord("A") for char in text.upper()
        ]  # Конвертируем каждую букву в число

    @staticmethod
    def _vector_to_text(vector):
        """Преобразует числовой вектор обратно в текст"""
        return "".join(
            chr(num + ord("A")) for num in vector
        )  # Конвертируем каждое число обратно в букву

    def _mod_matrix(self, matrix):
        """Вычисляет модуль матрицы по mod (для предотвращения отрицательных значений)"""
        return (
            matrix % self.mod
        )  # Берем остаток от деления каждого элемента матрицы на mod

    def _matrix_mult(self, matrix, vector):
        """Умножает матрицу на вектор и берет результат по модулю"""
        # Умножаем матрицу на вектор, затем берем остаток от деления каждого элемента результата на mod
        return self._mod_matrix(np.dot(matrix, vector))

    def encrypt(self, plaintext):
        """Шифрует текст, разбивая его на блоки"""
        # Преобразуем текст в числовой вектор
        vector = self._text_to_vector(plaintext)

        # Разбиваем вектор на блоки по размерности матрицы
        encrypted_vector = []  # Массив для хранения зашифрованных чисел
        block_size = self.encryption_matrix.shape[
            0
        ]  # Размер блока равен количеству строк в матрице

        # Дополняем текст до размера, кратного block_size
        # Если длина текста не делится на block_size, добавляем 'A' (0) до кратного размера
        while len(vector) % block_size != 0:
            vector.append(0)  # 'A' представлено как 0

        # Шифруем каждый блок
        for i in range(0, len(vector), block_size):
            block = vector[i : i + block_size]  # Берем блок длины block_size
            encrypted_block = self._matrix_mult(
                self.encryption_matrix, block
            )  # Умножаем матрицу на блок и берем mod
            encrypted_vector.extend(
                encrypted_block
            )  # Добавляем зашифрованный блок в общий вектор

        # Возвращаем зашифрованный текст
        return self._vector_to_text(encrypted_vector)

    def decrypt(self, ciphertext):
        """Расшифровывает текст, разбивая его на блоки"""
        # Преобразуем текст в числовой вектор
        vector = self._text_to_vector(ciphertext)

        # Разбиваем вектор на блоки по размерности матрицы
        decrypted_vector = []  # Массив для хранения расшифрованных чисел
        block_size = self.decryption_matrix.shape[
            0
        ]  # Размер блока равен количеству строк в матрице

        # Расшифровываем каждый блок
        for i in range(0, len(vector), block_size):
            block = vector[i : i + block_size]  # Берем блок длины block_size
            decrypted_block = self._matrix_mult(
                self.decryption_matrix, block
            )  # Умножаем матрицу на блок и берем mod
            decrypted_vector.extend(
                decrypted_block
            )  # Добавляем расшифрованный блок в общий вектор

        # Возвращаем расшифрованный текст
        return self._vector_to_text(decrypted_vector)


# Пример использования:
# Матрица M и её обратная M^-1 (из задания)
encryption_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

decryption_matrix = [[8, 5, 10], [21, 8, 21], [21, 12, 8]]

# Создаем объект класса HillCipher
cipher = HillCipher(encryption_matrix, decryption_matrix)

# Тестируем шифрование и расшифрование на примере текста
plaintext = """This is an example of the Hill cipher encryption and decryption.
It is designed to showcase the functionality of the algorithm."""
encrypted_text = cipher.encrypt(plaintext)  # Зашифрованный текст
decrypted_text = cipher.decrypt(encrypted_text)  # Расшифрованный текст

# Печатаем результаты
print(f"Оригинальный текст: {plaintext}")
print(f"Зашифрованный текст: {encrypted_text}")
print(f"Расшифрованный текст: {decrypted_text}")
