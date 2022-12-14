#Функции
def SayHello() :
    print("Привет, Мир!")

SayHello()
#Параметры функций
def printMax(a,b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, "равно", b)
    else:
        print(b, 'максимально')

printMax(5,8)

g = 5
j = 9

printMax(g,j)

#локальные переменные
x = 50
def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func(x)
print('x по прежнему', x)


#Зарезервированное слово Global
y = 20
def functt():
    global y
    print('y равно', y)
    y = 2
    print("Заменяем глобальное значение y на", y)

functt()
print('значение y составляет', y)


#Зарезервированное слово nonlocal
def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальный x сменился на', x)

func_outer()

#Значение аргументов по умолчанию
def say(message, times = 1):
    print(message * times)

say("Аким")
say("шмонька! ", 5)


#Ключевые аргументы
def func_key(a, b=5, c=10):
    print("a равно", a, "b равно", b, "c равно", c)

func_key(3, 7)
func_key(25, c=24)
func_key(c=50, a=100)