
number = 23
running = True

while running:
    guess = int(input('Введите целое число:'))

    if guess == number:
        print('Поздравляю! Вы угадали!')
        running = False
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print ("Нет, загаданное число немного меньше этого")
else:
    print("Цикл While закончен")

print('Завершено!')