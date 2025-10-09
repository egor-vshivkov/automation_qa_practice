user_input = input('your number: ')

if user_input.isnumeric():
    user_input = int(user_input)
    if user_input == 1:
        print('One')
    elif user_input == 2:
        print('two')
    elif user_input == 3:
        print('three')
    else:
        print('many')
else:
    print('Enter a number please')


user_input = int(input('your number: '))

if user_input == 1:
    print('One')

if user_input == 2:
    print('two')

if user_input not in [1, 2]:
    print('many')


if user_input > 0:
    if user_input > 1:
        if user_input == 2:
            print()
        elif user_input == 3:
            if 1 == 1:
                print()
            elif 2 == 2:
                print()
    elif 3 == 3:
        print()


names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

for name in names:
    print(name)

print('the end')


names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']


for name in names:
    name = name.replace('i', 'I')
    if name.startswith('J'):
        print('Mr.', end=' ')
    print(name)


names = ('John', 'Tim', 'James', 'Bob', 'Jim', 'Bill')
for name in names:
    print(name)


names = {'John', 'Tim', 'James', 'Bob', 'Jim', 'Bill'}
for name in names:
    print(name)


persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons:
    print(person)


persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.keys())
for person in persons.keys():
    print(person)


persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.values())
for person in persons.values():
    print(person)


persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons:
    print(f'{person}: {persons[person]}')


persons = {'John': 132, 'Tom': 167, 'James': 234}
for name, height in persons.items():
    print(f'{name}: {height}')


text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'

words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
        # words.remove(word)
    else:
        fin_words.append(word)

print(' '.join(words))
