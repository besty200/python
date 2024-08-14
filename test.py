name = input('Введите своё имя: ')
age = int(input('Введите свой возраст: '))
rost = float(input('Введите свой рост: '))
ves = int(input('Введите свой вес: '))
imt = ves/(rost**2)

print(f'Добрый день, {name}. Вам {age} лет и ваш индекс массы тела = {imt}')