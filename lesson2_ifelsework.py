'''
a=2**3
b=3**2

if a>b:
 	print('a bolshe', a)
elif b>a:
	print('b bolshe', b)
else:
	pass



a=int(input('vvedite chislo'))

if  a>0 and a<21 or a>57 and a<100:
	print('razresheno')
else:
	print('net')


'''
'''
a=int(input('vvedite chislo'))

if a%2==0:
	print('chetnoe vedite i')
	i=int(input('vvedite chislo'))
	if i%3==0:
		print('delitsya na 3 bez ostatka')
		c=int(input('vvedi chislo'))
		if a**2>1000:
			print('bolshe')
		elif a**2<1000:
			print('menshe')
	else:
		print('i ne del 3')

elif a%2!=0:
	if i%3==0:
		print("del")
		if a**2 > 1000:
			print(a,"> 1000")
		else:
			print ('a**2',a, "< 1000")
	elif a**2 > 1000:
		print(a,'> 1000, no ne del 3')

print('finish programm')
'''

'''
#otsuda nado proverit
#
a=int(input('vvedite znachenie,  '))

if a==1000:
	print('ravno 1000')
elif a>1000:
 	print('menshe 1000')
else:
	print('test')

'''

'''
#
a=10//5
b=10/5
c=a+b

if a>b:
	print('peremennaya a bolshe')
elif a<b:
	print('peremennaya b bolshe')
else:
	print(c)
'''


'''
#
a=int(input('vvedite znachenie'))

if a<0:
	print('otricatelnoe chislo')
elif a>0:
	print('polojitelnoe chislo')
else:
	print('test')

#7
a=10
b=5

if a>0 and b>0:
	print('peremennaya polojitelnaya')
elif a<0 and b<0:
	print('peremennaya otricatelnaya')
else:
	print('test')



#8
a=10
b=5
c=a+2
d=b+2

if a>b:
	print(c)
else:
	print(d)




#9

a=int(input('vvedite luboya chislo'))

if a>0:
	print('polojitelnoe chislo')
elif a<0:
	print('oticatelnoe chislo')
else:
	print(a)



#10
a=int(input('vash vozrast'))

if a>18 and a==18:
	print('sovershennoletniy')
elif a<18 and a==4:
	print('rebenok')
else:
	print('nesovershennoletniy')



#11
a=45
b=6

if a/b:
	print('chislo delitsya')
else:
	print('chislo ne delitsya')


#12
a=int(input('vvedite luboi god iz 4 simvolov'))

if a==2021:
	print('tekushiy god')
elif a>2021:
	print('god eshe ne nastupil')
else:
	print('god proshel')


#13
a=int(input('vash god rojdeniya'))

if a>18 and a==18:
	print('sovershennoletniy')
elif a<4 and a==4:
	print('rebenok')
else:
	print('nesovershennoletniy')



#14

a = int(input('vedi : '))
if a%2==0:
	print('chet')
else:
	print(' ne chet')
if a%3==0:
	print("del")
elif a%3!=0:
	print("ne del")
if a**2 > 1000:
	print("a  > 1000")
else:
	print("a < 1000")
'''

'''

Четвертое Задание 
Покупка машины
Хочу
лексус или тойоту от 2004 года с пробегом 150000 белую или серую с левым
рулем и максимум 2 хозяина и стоимостью не больше 10000 или такую же ,
но с пробегом 200000 и с ценой меньше 8000
<= 10000
Toyota Lexus
2004
150000
white grey
2
left
200000
< 8000
'''


d = input('Выберите на английском букву a, если хотите машину лексус или тойоту, от 2004 года с пробегом 150000, белую или серую, с левымрулем и максимум 2 хозяина и стоимостью не больше 10000 или введите букву b если хотите машину лексус или тойоту от 2004 года с пробегом 200000, белую или серую, с левым рулем и максимум 2 хозяина и стоимостью меньше 8000,   ')

a='1'
b='2'

if d==a:
	print('Вы выбрали машину a  это лексус или тойоту от 2004 года с пробегом 150000 белую или серую с левым рулем и максимум 2 хозяина и стоимостью не больше 10000')
elif d==b:
	print('Вы выбрали машину b это лексус или тойоту от 2004 года с пробегом 200000, белую или серую с левым рулем и максимум 2 хозяина и стоимостью меньше 8000')
else:
	print('Вы не хотели такую машину')



'''
if d == a:
        print('Вы выбрали машину a  это лексус или тойоту от 2004 года с пробегом 150000 белую или серую с левым рулем и максимум 2 хозяина и стоимостью не больше 10000')
if d==b:
        print('Вы выбрали машину b это лексус или тойоту от 2004 года с пробегом 150000 белую или серую с левым рулем и максимум 2 хозяина и стоимостью не больше 10000 но с пробегом 200000 и с ценой меньше 8000>
else:
        print('Вы не хотели такую машину')
'''

'''
d = (input('Выберите на английском букву a, если хотите машину лексус или тойоту, от 2004 года с пробегом 150000, белую или серую, с левымрулем и максимум 2 хозяина и стоимостью не больше 10000 или введите букв'>

a='1'
b='2'

if d==a:
        print('Вы выбрали машину a  это лексус или тойоту от 2004 года с пробегом 150000 белую или серую с левым рулем и максимум 2 хозяина и стоимостью не больше 10000')
elif d==b:
        print('Вы выбрали машину b это лексус или тойоту от 2004 года с пробегом 200000, белую или серую с левым рулем и максимум 2 хозяина и стоимостью меньше 8000')
else:
        print('Вы не хотели такую машину')
'''
