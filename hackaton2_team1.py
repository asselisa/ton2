#1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a[5:])
#2     
digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)

for i in digits:
        print(i/9)
#3
fruits = ('banana','stawberry','apple','orange','limon','ananas')

print(fruits[0::5])
#4       
 spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

w=set(spisok_1)
e=set(spisok_2)
a = e.difference(w)
print(a)


#5
# # 5
# # i = 0
# # while i<300:
# #     if i%2==0:
# #         print(i)
# #     if i == 237:
# #         break
# #     i+=1


# 6
# from random import *
# a = input("Выберите число от 0 до 10")
# x = randint(0,10)
# if x != a:
#     print(f"Компьютер выбрал {x}, Проигрыш!")
# else:
#     print(f"Вы выиграли! Компьютер выбрал, {x}")


#6
#7
d=" "
while len(d)<6 and d.split()<6:
        d= list(input("Введите предложение"))
        if len(d)>6 and d.split()>6:
                d.append(d)


#problem8
'''numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
w=[]
for i in numbers:
        if i%2==0:
                w.append(i)
print(len(w))
s=[]
for i in numbers:
        if i%2!=0:
                s.append(i)
print(len(s))'''

#problem9
'''numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
b=[]
for i in numbers:
        if i<0:
                b.append(-1)
        if i>0:
                b.append(1)
print(b)'''

#10
a =[2,4,6,8,10,1,3,5,7,9,11,13,17] 
print(a[::2])

#11
a =[1,0,-2,4,3,6,6,3,5,8,4,2] 
print(sorted(a))
