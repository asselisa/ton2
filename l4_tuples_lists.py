'''
a=[1,35,6.5]
print(min(a)/len(a))

a=[1,35,6.5,True,'str']
b=a.append('hello')

print(a)

print(a.index(True))

print(a.pop(2))
print(a)

print(a[0:4])#nachinaya c 0

print(a[0:5:2])

print(a[3::2])

print(a[a:4])

p(a[1;6:2])

p(a[1::-1])

p(a[:len(a)//2]) #delenie po  modulu on budet brat celoe pervuy cifru, ostatok ne budet brat

'''
'''
#0
a=(0,1,2,3,4,5,6,7,8,9,10)
b=('a','b','c','d','e','f','g','h','i')
c=(10,11,12,13,14,15,16,17,18,19)
d=(а, б, в, г, д)
c=(100, 101, 102, 103, 104, 105)
'''


'''
#1
b=('a','b','c','d','e') #esli net kovichek budet dumat chto eto peremennaya
print(d[0:4])
'''

'''
#2
a=[1, 2.5, True, 'str']

'''

'''
#3
a=['Yana','Nursultan','Asel','Eliza','Altinay']
b='Ufuk'
print(b.join(a))
'''

'''
#4
a=['Yana','Nursultan','Asel','Eliza','Altinay']


b=['a','b','c','d','e','f','g','h','i']
a.append(b)
print(a)

#5
names=[]
print(names.count('Jack'))


#6

names.remove('Jack')
print(names)


while 'Jack' in names:
	names.remove('Jack')
print(names)


#7
a=[]
a.append(input('vashe imya:'))
a.append(int(input('Vozrasty: ')))
a.append(input('leng: '))
print(a)
a.pop(1)
print(a)
a.append('hello')
print(a)

#8

pythonlist = ["","", "", "", "", "", "None", True, False]
a=pythonlist.index('loop')
pythonlist.pop(a)
print(pythonlist)
'''
#9

a=[5,6,7,8]
print(a[0]*a[1]*a[2]*a[3])
































































