a = 1

a += 1
# a = a + 1

print(a)

print('text' + 'text')
text = 'text'
# text = text + ' new'
text += ' new'
print(text)
symbol = '='
# symbol = symbol * 20
symbol *= 30
print(symbol)
print('Copyrights')
print(symbol)

text = 'I love Python!'
print('love' in text)
print('Love' in text)

b = 2
print(id(b))
c = 2
print(id(c))
d = 257
print(id(d))
e = 257
print(id(e))
print(b is c)
print(d is not e)

input('What is your name?')
a = 1

user_name = input('What is your name?')
print('Hello', user_name, '!')

user_input = int(input('Enter a number'))
print(type(user_input))

print(2 + user_input)

a = '1'
print(type(a))
a = int(a)
print(type(a))
a = str(a)
print(type(a))
b = 'True'
print(type(b))
b = bool(b)
print(type(b))
a = float(a)
print(type(a))
print(a)

my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last', 'last2']
print(my_list)
print(my_list[2])
print(my_list[0])
print(my_list[9])
print(my_list[-1])
print(my_list[-3])

my_list[2] = 42
print(my_list)

my_list = []
my_list = list()
my_list.append(42)
my_list.append('text')
print(my_list)
print(len(my_list))
print(my_list.index('text'))
poped = my_list.pop(0)
print(my_list)
print(poped)

print(42 in my_list)

my_tuple = (1, 3, 6, 7, None, 'text', False, 2.42)
print(my_tuple[2])
print(my_tuple[-1])
# my_tuple[4] = 42

my_tuple = ()
my_tuple = tuple()
my_tuple = (1, 5, 2, 6, 1)
print(my_tuple)
print(my_tuple.count(1))
print(my_tuple.index(5))

llist = [56]
print(llist)
ttuple = (56,)
print(ttuple)
print(type(ttuple))

my_set = {1, 3, 6, 7, None, 'text', False, 2.42, 3, 7}
# print(my_set[2])
my_set.add(42)
my_set.add('text')
print(my_set)

list1 = list(set([1, 2, 5, 6, 2, 1, 8]))
# list1 = set(list1)
# list1 = list(list1)

print(list1)

my_set = {} # Это словарь
print(type(my_set))
my_set = set() #  Пустой set можно создать только так
print(type(my_set))

my_dict = {'one': 'value', 'two': 'value2'}
print(my_dict['one'])
print(len(my_dict))
my_dict['one'] = 'myvalue'
my_dict['three'] = 'value3'
my_dict['four'] = False
my_dict['five'] = [1, 5, 8]
my_dict['six'] = {1, 6, 9}
my_dict[2] = 'skldjflskdf'
my_dict[False] = 'skdjhskdjf'
my_dict[2.42] = 'werwerw'
my_dict[(1, 2)] = 'ieruyieurtert'
my_dict[5] = {1: 2}



print(my_dict)
print(type(my_dict))

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
