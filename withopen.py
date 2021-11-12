"""
#1  С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir. В итоге у вас на рабочем столе должен
# появиться файл directories.txt. Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

a=open('/home/assella/Рабочий стол/directories.txt', 'w')
a.write('''
lrwxrwxrwx   1 root root          7 Қаз 30 03:32 bin -> usr/bin
drwxr-xr-x   4 root root       4096 Қаз 30 03:35 boot
drwxrwxr-x   5 root root       4096 Қаз 31 06:48 cdrom
drwxr-xr-x  21 root root       4560 Қар 10 18:32 dev
drwxr-xr-x 130 root root      12288 Қар  8 15:48 etc
drwxr-xr-x   3 root root       4096 Қаз 31 06:57 home
drwxr-xr-x   2 root root       4096 Қаз 31 06:36 html
lrwxrwxrwx   1 root root          7 Қаз 30 03:32 lib -> usr/lib
lrwxrwxrwx   1 root root          9 Қаз 30 03:32 lib32 -> usr/lib32
lrwxrwxrwx   1 root root          9 Қаз 30 03:32 lib64 -> usr/lib64
lrwxrwxrwx   1 root root         10 Қаз 30 03:32 libx32 -> usr/libx32
drwx------   2 root root      16384 Қаз 30 03:31 lost+found
drwxr-xr-x   3 root root       4096 Қар  2 19:21 media
drwxr-xr-x   2 root root       4096 Ақп 10  2021 mnt
drwxr-xr-x   2 root root       4096 Ақп 10  2021 opt
dr-xr-xr-x 358 root root          0 Қар 10 18:32 proc
drwx------   4 root root       4096 Қаз 30 09:37 root
drwxr-xr-x  35 root root        980 Қар 10 18:33 run
lrwxrwxrwx   1 root root          8 Қаз 30 03:32 sbin -> usr/sbin
drwxr-xr-x   9 root root       4096 Қар  2 19:13 snap
drwxr-xr-x   2 root root       4096 Ақп 10  2021 srv
-rw-------   1 root root 2147483648 Қаз 30 03:32 swapfile
dr-xr-xr-x  13 root root          0 Қар 10 18:32 sys
drwxrwxrwt  21 root root       4096 Қар 10 19:56 tmp
drwxr-xr-x  14 root root       4096 Ақп 10  2021 usr
drwxr-xr-x  14 root root       4096 Ақп 10  2021 var
drwxr-xr-x   2 root root       4096 Қаз 31 06:36 www

''')"""

"""
#2 Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.

file=open('/home/assella/Рабочий стол/users.txt', 'a')
a=input('username: ')
w=input('parol: ')
s=file.write(f'username:  {a} password: {w}')
file.close()
"""

#3 Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. 
#Подсказка: используйте ключевое слово in.

a=open('users.txt', "a") 
if "w" in a.read:
	print("da est")
else:
	print("net")





'''
file = open('insta.txt', 'a+')
a=input('username: ' )
w=input('parol: ')
s=file.write(f'username: {a} password: {w}')
file.close()


with open('insta.txt', 'a') as file:
	a=input('username: ')
	w=input('parol: ')
	file.write(f'username: {a}')
	file.write(f'password: {w}')
'''






'''
print(«nujno sdelat site skolko eto budet stoit»)
a = int(inpu

file = open(«ap.txt», «r»)
print(file.read())

open — sozdaet create

file = open(«ap.txt», «r»)
a= input(„username: “)
w=input(«parol: »)
s=file.write(f“username: {a} \npassword: {w}\n“)
file.clos()


oss = open(«hunter.txt»,»a+»)
print(oss.write(«nedokon»))


with open(«insta.txt», «r») as a:
	print(a.read())

with open(«insta.txt», «r») as file:
	print(file.read())

file =open(«/itc/insta.txt»)

with open(„insta.txt“, «a») as file:
	a=input(«username: »)
	w=input(«parol: »)
	file.write(f»username:  {a}»)
	file.write(f»password:  {w}»)

file=open(«insta.txt», „r“)

for i in range(5,100,10):     ot 5 do 100 , potom s shagom 10 po 10 dobavlyaet 15, 25, 35 i td
	print(i)

'''
