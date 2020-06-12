# Date: 11/06/2020

# Exercises of the first module: Lists, Tuples, Dics

# Exercise 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Exercise 2
print(bicycles[1])

# Exercise 3
print(bicycles[1].capitalize())

# Exercise 4
print(bicycles[-1])

# Exercise 5
print('My first bicycle was a {}'.format(bicycles[0].capitalize()))

# Exercise 6
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Exercise 7
motorcycles[0] = 'ducati'

# Exercise 8
motorcycles.append('honda')
print(motorcycles)

# Exercise 9
motorcycles.pop(0)
print(motorcycles)

# Exercise 10
motorcycles.insert(0,'ducati')
print(motorcycles)

# Exercise 11
motorcycles_popped = motorcycles.pop()
print(type(motorcycles_popped))

# Exercise 12
motorcycles.remove('yamaha')
print(motorcycles)

print('\n------------------------------------------------------------\n')

# Exercise 13
motorcycles = []
motorcycles.extend(['yamaha', 'ducati', 'suzuki', 'ducati', 'ducati'])
print(motorcycles)
while 'ducati' in motorcycles:
    motorcycles.remove('ducati')
print(motorcycles)

# Exercise 14
motorcycles = ['yamaha', 'suzuki', 'honda', 'ducati']
motorcycles.sort()
print(motorcycles)

# Exercise 15
motorcycles = ['yamaha', 'suzuki', 'honda', 'ducati']
motorcycles_sort = sorted(motorcycles)
print('Original list:',motorcycles,'and sort list:',motorcycles_sort)

# Exercise 16
print('Motorcycles has {} elements'.format(len(motorcycles)))

# Exercise 17
for i in motorcycles:
    print(i)

motorcycles.reverse()
for i in motorcycles:
    print(i)

# Exercise 18
print('motorcycles[4] gives error out of index because the last item is in the position 3')

# Exercise 19
print(motorcycles[-1])
print('Returns the last item of the list')

# Exercise 20
print(motorcycles[1:3])

# Exercise 21
print(motorcycles[1:])

# Exercise 22
print('\n------------------------------------------------------------\n')
my_foods = ['pizza', 'cakes', 'meat']
family_foods = my_foods

print('My favorite foods are:', ', '.join(my_foods))
print("My famil's favorite foods are:", ', '.join(family_foods))

# Exercise 23
my_foods.append('ice-cream')
print(my_foods)
print(family_foods)

# Exercise 24
word = input('Please, introduce a word: ')
word = 'la'
vowels = ['a', 'e', 'i', 'o', 'u']
found=[]
for i in word:
    if i in vowels:
        found.append(i)
print(found)
print(list(set(found)))

# Exercise 25
print('\n------------------------------------------------------------\n')
dimensiones = (100,200)
print(dimensiones, type(dimensiones))

# Exercise 26
print(dimensiones[0], type(dimensiones[0]))

# Exercise 27
for i in dimensiones:
    print(i)

# Exercise 28
print('\n------------------------------------------------------------\n')
name = input('Please, introduce your name: ')
address = input('Please, introduce your address: ')
age = int(input('Please, introduce your age: '))
phone = int(input('Please, introduce you phone number: '))

keys = ['name', 'address', 'age', 'phone']
values = list([name,address,age,phone])

person = dict([('name', name), ('address', address), ('age', age), ('phone', phone) ])
person_1 = dict(zip(keys,values))

print('{} tiene {} años, vive en {} y su número de teléfono es {}.'.format(person['name'],
                                                                           person['age'],
                                                                           person['address'],
                                                                           person['phone']))

# Exercise 29
person = dict()

for i in range(0,100):
    key = input('What data do you want to introduce? ')
    value = input('What is your '+key+'? ')
    person[key]=value
    decision = (input('Do you want to introduce more information? (Yes/No) ')).lower()
    if decision == 'yes':
        pass
    else:
        break
print(person)

# Exercise 30
countries=['Spain', 'Poland', 'England', 'Switzerland']
money=['Euro', 'Zloty', 'Pound', 'Swiss Franc']
currences = dict(zip(countries, money))
country = input('Please, choose one of the following countries: '+', '.join(list(currences.keys()))+': ')
print('The currency of the country is:', currences[country.lower().capitalize()])

# Exercise 31
user_1 = '123'
user_2 = '124'
user_3 = '125'
keys = ['Name', 'Age', 'Email', 'Phone']
values_user_1 = ['Miguel', 24, 'miguel@gmail.com', '123']
values_user_2 = ['Juan', 24, 'juan@gmail.com', '124']
values_user_3 = ['Carlos', 24, 'carlos@gmail.com', '125']

dic_user_1 = dict(zip(keys,values_user_1))
dic_user_2= dict(zip(keys,values_user_2))
dic_user_3= dict(zip(keys,values_user_3))

app_dic = dict([(user_1, dic_user_1), (user_2, dic_user_2), (user_3, dic_user_3)])
print(app_dic)


