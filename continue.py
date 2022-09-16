while True:
    s = input('Введите что-нибудь : ')
    if s == ('выход'):
        break
    if len(s) < 3:
        print('слишком мало')
        continue
    print("Введенная строка достаточной длинны")
print('Завершение')