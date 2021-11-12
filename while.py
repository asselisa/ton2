'''
i=0
while i<9: # do teh por poka i budet ravno 9 to ti doljen dobavlyat po 2
	print(i)
	i+=1 #i=i+1
	if i==3:	
		break  #continute proidet do 3 i ne prekratitsya
	i=i+1


i=0
while i<10:
	i+=1
	if i==3 # 3 propustit i srazu k 4 idet
		continue
	print(i)

#for chasto ispolzuyt, while nachnet beskonechno zasoryat 


while True:
	n=input('Please enter hello')
	if n.strip() =='hello':
		break

spisok a=[1,2,5,9,20]
for цикл for i in a:  и каждый раз будет брать значение из списка и вместо введет i=1,2,3,9,20

for i in a:
	print(i)
	if i==9:
	break
metod range

for i in range(10):  # (5,25) ot 5 do 25
print(i)
 



for i in range(100):
	print(i)


a=[]
b='asel'
for i in range (6):
	ifa[]



a=['aidar','tima','bektur','beknazar','asel','azat']
b='asel'

for i in a:
	if i ==b:
		print('yes',b)
	else:
		print('no asel:', i)
	if i == 'tima':
		print('ostanovleno')
		break   #a.append('chika') print(a) ili, continue# ostanovilzya v time i dalshe poshel po spisku #a.remove('asel') print(a)








a=['aidar','tima','bektur','beknazar','asel','azat']
b='asel'

for i in a:
        if i ==b:
                print('yes',b)
        for i in a:
        if i == 'bektur':
		a=0
		while a<=10: #10 nije 0 poetomu beskonechno  bektur napisal
		print(f,end="")
               	a+=1  #print('1*10')  #print(f{i}, end=" ")
	else:
		print('no asel:', i)
               
ctrl z chotobi beskonechno ne poshel


'''


'''
#1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for i in languages:
	if i==lang1:
		print('yes', lang1)
	else:
		print('no rust in the list') 
'''



'''
#2
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for languages in range(7):
	if languages=='php':
		break
'''

for i in languages:
	print(i)
	if i =='php':
		break

'''

#3  3. Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз. 

a=7
for i in range(5): #skolko raz doljen vipolnitsya  range 5
	a=a*7
	print(a)
	#i=i**5 
'''


'''
#4  4. Напишите код, который выведет на экран список языков с нумерацией.
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#Вывод:  # 0 go  1 java   2 php   3 python  4 javascript   5 ruby

for i, languages in enumerate(languages):
	print(i, languages)

#5  5. Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1      Усиление: Получите такой же результат но с ОДНИМ циклом		

#end v odnu stroku delaet

for i in range(-9,10):
	print(10-abs(i), end='')

'''


'''
i=0
while i<=9:
	print(i, end='')
	i+=1
while i !=0:
	print(i, end='')
	i -=1
'''




for i in range(1,11):
	print(i,9-abs(i-1))






#6
lubaya peremennay kotoraya ravnyaetsya 0
i esli eto peremennaya menshe dlini   poka  0 budet menshe dlini spiska proveryai po etim kriteriyam
poka 0 menshe dlini

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
i=0
while i<len(names):
	if i % 2 ==0:
	print(names[i])
	i=i+1

#
for i in range(300):
	if i%7==0 or i%5==0:
		print(i)
	
	if i == 254:
		print("мы нашли цифру 255 и остановились")
		break






for i in range(300):
        if i%10==7:
		print(i)
 


s=0
for i in range(300):
        if i%10==7:
                print(i)
 		s+=1
		print(s, "kolichestvo 7")
