# Задание №1:
# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23 (3+5+6+9) = 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

'''
a=0
for i in range(1,1000):
	if i%3==0 or i%5==0:
		a+=i #
print(a)
'''





# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №2:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.

'''
b=0
for i in "4729461084":
	b+=int(i)
print(b)
'''





# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №3:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты:

# date = {
# "year": "2020",
# "month": "10",
# .....
# }

b={'god': input('vvedi god'),
'месяц': input('vvedi month'),
'day': input('vvedi day')}
print(b)





# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №4:
# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?

'''
a='1'
if a*5:
'''





# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №5:
# Напишите команду Linux которая создаст ДИРЕКТОРИЮ в НЕСУЩЕСТВУЮЩЕЙ директории БЕЗ ОШИБОК!






# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №6:
# Как в Linux выглядит полный путь до Desktop Директории для пользователя 'developer'.
