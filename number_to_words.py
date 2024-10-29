def number_in_words(number):
    # Ограничение для ввода миллиарда
    if number > 999_999_999 or number < -999_999_999:
        return "Ошибка: допустимый диапазон от -999_999_999 до 999_999_999"

    if number < 0:
        number = abs(number)

    num_in_words = ""

    if number >= 1_000_000:
        millions, number = divmod(number, 1_000_000)
        num_in_words = fold(num_in_words, convert_hundreds(millions))
        num_in_words = fold(num_in_words, "миллион" if millions % 10 == 1 and millions % 100 != 11 
                            else "миллиона" if 2 <= millions % 10 <= 4 and (millions % 100 < 10 or millions % 100 >= 20)
                            else "миллионов")

    if number >= 1_000:
        thousands, number = divmod(number, 1_000)
        num_in_words = fold(num_in_words, convert_hundreds(thousands))
        num_in_words = fold(num_in_words, "тысяча" if thousands % 10 == 1 and thousands % 100 != 11 
                            else "тысячи" if 2 <= thousands % 10 <= 4 and (thousands % 100 < 10 or thousands % 100 >= 20)
                            else "тысяч")

    if number > 0:
        num_in_words = fold(num_in_words, convert_hundreds(number))

    return num_in_words


def fold(str1, str2):
    return str2 if not str1 else str1 + " " + str2


def convert_hundreds(number):
    result = ""
    if number >= 100:
        hundreds, number = divmod(number, 100)
        result = fold(result, num_to_words[hundreds * 100])

    if number >= 20:
        tens, number = divmod(number, 10)
        result = fold(result, num_to_words[tens * 10])

    if number > 0:
        result = fold(result, num_to_words[number])

    return result


num_to_words = {
    1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
    6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
    11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
    16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать",
    20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят",
    70: "семьдесят", 80: "восемьдесят", 90: "девяносто",
    100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот",
    600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот"
}

print(number_in_words(int(input("Введите число (до 999_999_999): "))))
