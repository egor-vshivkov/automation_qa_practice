import random
import datetime


summer = True

if summer is True:
    print('The weather is fine')
else:
    print('The weather is not fine')

summer = random.choice([False, True])

if summer:
    print('The weather is fine')
else:
    print('The weather is not fine')

a = 0

if a is not None:
    print('...')


numbers = [1, 45, 23, 67, 32, 89]
print(max(numbers))

# max_num = 0
# for x in numbers:
#     if x > max_num:
#         max_num = x

# print(max_num)

print(min(numbers))
print(sum(numbers))

a = 1 / 3
print(round(a, 2))

print(abs(1))

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

my_list = [1, 2, 3, 4, 5]

new_list = []
for x in my_list:
    new_list.append(x * 2)

print(new_list)

my_list = [1, 2, 3, 4, 5]

def mult_by_2(x):
    return x * 2

new_list = map(mult_by_2, my_list)
print(list(new_list))

my_list = [1, 2, 3, 4, 5]


new_list = map(lambda x: x * 2, my_list)
print(list(new_list))

name, surname = input('Your name and surname').split()
print(f'name is {name}, surname is {surname}')

code, number = map(int, input('code and number').split())
print(f'name is {code + 1}, surname is {number + 2}')

my_list = [1, 2, 3, 4, 5]

def mult_by_2(x):
    if x > 10:
        return x * 5
    else:
        return x * 2

new_list = map(lambda x: x * 5 if x > 10 else x * 2, my_list)
print(list(new_list))

my_list = [1, 2, 3, 4]
b = 1 if len(my_list) > 4 else 5

print(b)

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

new_list2 = []
for x in my_list2:
    if x % 2 == 0:
        new_list2.append(x)

print(new_list2)

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


new_list2 = filter(is_even, my_list2)
print(list(new_list2))

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(x):
    return x % 2 == 0


new_list2 = filter(is_even, my_list2)
print(list(new_list2))

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]


new_list2 = filter(lambda x: x % 2 == 0, my_list2)
print(list(new_list2))

time_now = datetime.datetime.now()
print(time_now)
print(time_now.hour)
print(time_now.year)
print(time_now.isoweekday())
print(time_now.timestamp())

easy_date = datetime.datetime(1360, 1, 15)
print(easy_date)
print(easy_date.timestamp())

my_time = '2023/06/05 12 hours, 30 mins, 10 secs'

python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')

print(python_date)
print(python_date.month)

human_date = python_date.strftime('Year: %y, month: %B, day: %d')
print(human_date)
