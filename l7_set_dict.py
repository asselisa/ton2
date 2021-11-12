'''
a={1, "Aidar", False, 1}
print(a, type(a))

a=set([1, 'python',False])
print(a, type(a))

a={'hello'}
b=("lol", 'admin')
a.add("world", "lol")
print(a)


a={'apple','amazon'}
v={'tesla','alibaba'}
a.update(v)
print(a)


a={'apple','amazon'}
v={'tesla','alibaba', 'apple'}
b=a.intersection(v)
print(b)


language = {'python', 'java', 'c', 'js'}
language.remove('java')
print(language)

a={'','','',a={'apple','amazon'}
v={'tesla','alibaba', 'apple'}
z=v.difference(a)
print(z)

a={'apple','amazon'}
v={'tesla','alibaba', 'apple'}
v.intersection(v)
print(b)

a={'apple','amazon'}
a.clear()
print(a)


v={'tesla','alibaba', 'apple'}
v.discard('tesla')
print(v)


a={'apple','amazon'}
v={'tesla','alibaba', 'apple'}
a.pop()
print(a)

'''


'''
#0
a={1,2,3,4,5,6,7}
a.remove(7)
print(a)
'''

'''
#1

farm_1 = {"dog", "cat", "mouse", "sheep"}
 
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

farm_1.intersection(farm_2)
print(farm_1)
'''

'''
#2
farm_1 = {"dog", "cat", "mouse", "sheep"} 
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1.difference(farm_2)
print(farm_1)
'''

'''
#3
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_2.add("chicken")
farm_2.pop()
print(farm_2)
'''

'''
b={
1 : "Chika", 
2 : "Amanda"
}
print(b)

b={
"student" : "Chika", 
1 : "Amanda"
}
print(b, type(b))


d={
1: {'students1': "Aidar", "students2":"Aybek"}
}
d.clear()
print(d)


d={
1: {'students1': "Aidar", "students2":"Aybek"}
}
a=d.get("students1")
print(a)

c={
"ok": "python"
}

v=c.keys()
print(v) #keys dlya klucha #valuesdlya



c={
"ok": "python",
"lol":"world"
}

v=c.get("lol")
print(v) 


company = {
1: "apple",
2: "amazon",
3: {"netflix":"kalmar"},
4: "alibaba"
}
c=company.get(2)
print(c) #values vitskivaet vseh

#get obrashenie k kluchu   #.values()

#items
company = {
1: "apple",
2: "amazon",
3: {"netflix":"kalmar"},
4: "alibaba"
}
c=company.items(2)
print(c) #values vitskivaet vseh
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
a=menu.update({'beshbarmak': 130})
print(menu)


#update
company = {
1: "apple",
2: "amazon",
3: {"netflix":"kalmar"},
4: "alibaba"
}
company.update({5:"google"})
c=company.get(2)
print(c) #values vitskivaet vseh


'''


#000
 
# # Словарь №1: dictionary key and value obyazatelno
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
a=menu.update({'beshbarmak': 130})
menu.update({'beshbarmak': 135})
menu.pop('borsh')
menu.update({'drinks':{ 'coca', 'sprite', 'fanta'}})
print(menu)
 



# a = input("Number a: ")
# symbol = input("What to do? ")
# b = input("Number b: ")
 
# if symbol == '+':
#   print(int(a) + int(b))





















































