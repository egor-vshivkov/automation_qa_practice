my_list = [1, 3]
my_tuple = (2, 6, 9)
# a = my_list[0]
# b = my_list[1]
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]
a, b = my_list
c, d, e = my_tuple
print(a, b, c, d, e)

lll = [1, 3, 5, 2, 5, 7 ,1, 3]
print(lll)
print(lll[1:4])
print(lll[:4])
print(lll[3:])
print(lll[1::2])
print(lll[:])
print(lll[::-1])
print(lll[::-2])
print(lll[-2:-6:-1])

text = 'my long long string'
print(text[3])
print(len(text))
print(text.index('long'))
print('long' in text)
print(text.count('n'))
print(text.count('long'))
print(text.find('lone'))
print(text[:7])
print(text.startswith('my'))
print(text.endswith('string'))

txt = "ThIs tExt wiTh meSsEd uP CaPITalIZatiOn!"
print(txt.capitalize()) # Делает первую букву предложения заглавной
print(txt.title())  # Делает каждую первую букву заглавной
print(txt.upper())  # Делает все буквы большими
print(txt.lower())  # Делает все буквы маленькими

text = 'mY lOng loNg STRING'
string_index = text.lower().index('string')
print(text[:string_index].lower() + text[string_index:].upper())

msg = 'Hello world!'
msg = msg.replace('world', 'universe')
print(msg)

data = '12,3'
data = data.replace(',', '.')
print(data)

txt = ' admin '
# txt = txt.replace(' ', '')
# txt = txt.strip()
# txt = txt.lstrip()
txt = txt.rstrip()
print(txt)
text = '"name"'
text = text.strip('"')
print(text)

my_string = 'some little text'
my_string2 = 'some,little,text'
list_from_text = my_string.split()
list_from_text2 = my_string2.split(',')
print(list_from_text)
print(list_from_text2)

languages = ['Python', 'Java', 'Ruby']
print(languages)
# languages = ', '.join(languages)
print(languages)
print('Student knows these languages:', ', '.join(languages))

a = 'one'
b = 'two'
print('First word is', a, ', second word is', b)


my_text = 'First word is ' + a + ', second word is ' + b
print(my_text)

my_text = 'First word is %s, second word is %s'
print(my_text % (a, b))

#string format
my_text = 'First word is {}, second word is {}'
print(my_text.format(a, b))

my_text = 'First word is {1}, second word is {0}'
print(my_text.format(a, b))

#f-string
my_text = f'First word is {{a}}, second word is {b}'
print(my_text)

template = 'Hello, {0}!'
# print(f'Hello, {username}!')
username = input('What is your name?')

print(template.format(username))

a = 'qwe'
b = 'asd'

my_text = 'First word is {{}}, second word is {}'
print_text = my_text.format(b)
print(print_text)

print(print_text.format('qqqqq'))
