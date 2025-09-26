flags = {
    'ru':{'red blue', 'white'},
    'kg':{"red yellow", 'red'},
    'ua':{"red blue", 'red', 'blue'},
    'uk':{"yellow", "blue"},
    'kz':{'blue yellow', 'blue'},
    'tr':{'red', 'wite'},
    'de':{'black', 'yellow'},
    'fr':{'red', 'blue'},
}

while True:
    user_input = input("Введите цвета флагов на англиском языке ").lower()

    if user_input == 'выход':
        break

    for key, value in flags.items():
        if user_input in value:
            print(key)