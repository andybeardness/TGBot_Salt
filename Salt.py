# Нужон для быстрой замены через регулярки
import re

# Основной класс, чтоб меньше кода было
class Vowels_S:

# Инициализация
    def __init__(self):
        # Получаем стринги русских глассных и солёной буквы
        self.RUS = self.get_rus()
        self.ENG = self.get_eng()

        # Создаём списки гласных + буква
        self.vowels_rus, self.s_rus = self.get_vowels(self.RUS[0], self.RUS[1])
        self.vowels_eng, self.s_eng = self.get_vowels(self.ENG[0], self.ENG[1])

        # Создаём списки из рус и англ гласных
        self.arr_vowels = [self.vowels_rus, self.vowels_eng]
        self.arr_s = [self.s_rus, self.s_eng]

    # Тут просто получаем гласные для:
    # РУС
    def get_rus(self):
        return 'аеёиоуыэюя', 'с'

    # АНГЛ
    def get_eng(self):
        return 'aeiouy', 's'

    # Делаем из:
    # ('аеёиоуыэюя', 'c')
    # Такое:
    # (['а', 'е', 'ё', 'и', 'о',
    #   'у', 'ы', 'э', 'ю', 'я'], 'c')
    def get_vowels(self, vowels_str, s_str):
        vowels = vowels_str
        vowels = list(vowels)
        s = s_str
        return vowels, s

    # Функция для перевода в солёный для одного языка
    def text_to_salt(self, text, vowels, s):
        result = text.lower()
        for char in vowels:
            result = re.sub(f'{char}', f'{char}{s}{char}', result)
        return result

    # Финальная функция
    # Там цикл для прогона по всем языкам
    def salt(self, text):
        result = text
        for vowels, s in zip(self.arr_vowels, self.arr_s):
            result = self.text_to_salt(result, vowels, s)
        return result