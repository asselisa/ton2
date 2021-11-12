

'''
int целые
float дробные
str 'hello world',   тройные для огромного текста когда не помещаются, одинарные и двойные скобки разницы нету
boolean true/false


a=''
print(type(a))


a='hello world'
print(a.lower())
print(a.title()) #sdelaed Hello World te zaglavnimi
print(len(a))

a = 'hello {name: }, how are you'
print(a.format(name='Asel'))

a= 'My name is {name}, I am {age}'.format(name='Asel', age=21)
print(a)

a='Hello'
d=a.center(20) #po probelam schitaet 20
print(d)


p='Aidar'
c='Aybel'
print(p+c)

a='2'

print(a+'2')


l='Bektur'
c='Chika'.join(l)
d=c.join(l)
print(c)

a='helo python'
s=a.startwith('h')  .endswith
print(s)



#0
a='sozdat '.lower()
b='predlojenie'.upper()
print(a+b)



#
a=True
print(str(a))



a=(input('vvedite simvol'))

b='Github'

if a in b:
	print(a.join(b)) # '(b.split(a))'
else:
	print('etogo znacheniya net')

'''

'''
a=(input('vv simv'))
print(f'GIT {a} HUB')

'''

'''
# #Строка №1:
# 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
# #Строка №2:
# 'Integers Floats Strings Lists Tuples'
# #Строка №3:
# 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
# #Строка №4:
# 'GitHub'
# #Строка №5:
# 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
# #Строка №6:
# 'Самые важные собЫтия в миРе инфосека за сентябрь'
# #Строка №7:
# 'Прошли те времена, когда компьютер был грязно-белой офисной коробкой.'
# Строка №8:
# "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
'''

'''

#3

a='Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
b='3'
print(a.replace("е",b))
'''
'''
if a=='e':
	print(a.replace('e',3))
else:
	print('test')


'''


'''
#4
a=(input('Vashe imya'))

b=int(input('Vash vozrast'))

c=(input('lubimiy film'))

print(a, "dobro")
print(b, 'great age')
print(c, 'wondeful film')

'''

'''
#cherez format #cherez f stroku toje sdelat
#4
a=input('Vashe imya: ')

b=int(input('Vash vozrast: '))

c=str(input('lubimiy film: '))

print(f'Здраствуйте {a}, Прекрастый возрост {b}, Классный фильм {c}!!!')

'''








'''
#5 ok
a='Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(len(a))
'''

'''
#6 ok
a='Самые важные собЫтия в миРе инфосека за сентябрь'
b='|'.join(a)

print(b)
'''



'''
#7 ok
a='хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(a.upper())
'''



'''
#3
a=1753
b=3

if a//3!=0:
	a = a/3
	print(a)
	if a//3!=0:
		print(a)
		a=a/3
		if a//3!=0:
			print(a)
			a = a/3
			if a//3!=0:
                		print(a)
                		a=a/3
				if a//3!=0:
					print(a)
					a=a/3
					if a//3!=0:
						print(a)

'''


'''
#cikl  // budet brat tolko celoe chislo   %smotret i brat tolko ostatki
a = 17531
b = True
s = 0
while b == True:
	if a//3!=0:
		a = a/3
		s +=1
		print(a)		
	if a//3==0:
		b == False
		print(s)
		break
'''

'''
while True: print(eval(input("Ведите выражение: ")))
'''


