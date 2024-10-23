class CaesarCipher:
    def __init__(self, shift):
        # Инициализируем объект, задаем величину смещения и алфавит
        self.shift = shift
        # Алфавит
        self.alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        # Длина алфавита, используется для корректного вычисления смещения
        self.alphabet_size = len(self.alphabet)

    def encrypt(self, text):
        # Метод для шифрования текста
        encrypted_text = ""  # Переменная для хранения зашифрованного текста
        for (
            char
        ) in (
            text.upper()
        ):  # Проходим по каждому символу текста, переводим в верхний регистр
            if char in self.alphabet:
                # Если символ в алфавите, находим его индекс
                index = self.alphabet.index(char)
                # Вычисляем новый индекс с учетом смещения, применяем модуль для циклического перехода
                new_index = (index + self.shift) % self.alphabet_size
                # Добавляем символ из алфавита с новым индексом в зашифрованный текст
                encrypted_text += self.alphabet[new_index]
            else:
                # Если символ не в алфавите (например, пробел, знак препинания), оставляем его без изменений
                encrypted_text += char
        # Возвращаем зашифрованный текст
        return encrypted_text

    def decrypt(self, text):
        # Метод для расшифрования текста
        decrypted_text = ""  # Переменная для хранения расшифрованного текста
        for (
            char
        ) in (
            text.upper()
        ):  # Проходим по каждому символу текста, переводим в верхний регистр
            if char in self.alphabet:
                # Если символ в алфавите, находим его индекс
                index = self.alphabet.index(char)
                # Вычисляем новый индекс с учетом обратного смещения
                new_index = (index - self.shift) % self.alphabet_size
                # Добавляем символ из алфавита с новым индексом в расшифрованный текст
                decrypted_text += self.alphabet[new_index]
            else:
                # Если символ не в алфавите, оставляем его без изменений
                decrypted_text += char
        # Возвращаем расшифрованный текст
        return decrypted_text


# Проверка работы алгоритма на примере
# Указываем величину смещения (например, номер группы + 2 = 3)
shift_value = 3
# Создаем объект класса с заданным смещением
cipher = CaesarCipher(shift=shift_value)

# Пример текста для шифрования
example_text = "Пример текста для демонстрации работы алгоритма Цезаря на русском языке. Это просто пример."

# Шифрование текста
encrypted_text = cipher.encrypt(example_text)
print(f"Зашифрованный текст: {encrypted_text}")

# Расшифрование текста
decrypted_text = cipher.decrypt(encrypted_text)
print(f"Расшифрованный текст: {decrypted_text}")
