# import random
from random import random, randint, randrange, choice
# from random import *
from helper import assist as assist1
from help2 import assist as assist2
from help2 import very_useful_function_for_your_easy_life as useful


def generate_text(text1, text2):
    return f'Text consists on the wrods:{text1} and {text2}'
    a = 1
print(generate_text('Ivan', 'Ivanov'))

my_list = [1, 2, 5, 7, 4, 9]

for x in my_list:
    print(x)

n = 2

progression = []
num = 1
while len(progression) < 100000000000000:
    progression.append(num)
    num += n

def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

# for number in progression(10):
#     print(number)
# print(list(progression(10)))

count = 1
for number in progression(1000000000):
    if count == 1000000:
        print(number)
        break
    count += 1


# print()
# input()
# int()

# print(random.random())
# print(f'Your price is {int(random.random() * 100)}')
# print(random.randint(0, 1))
# print(random.randrange(0, 10, 2))
# users = ['user11', 'user12', 'user100']
# print(random.choice(users))

print(random())
print(f'Your price is {int(random() * 100)}')
print(randint(0, 1))
print(randrange(0, 10, 2))
users = ['user11', 'user12', 'user100']
print(choice(users))

assist1()
# print(helper.variable)
while 'sldkjfl' == 'sdsdfsdf':
    if 'sldkjfl' == 'sdsdfsdf':
        print(f'skadflkasdjfhalsdkjhlaksdfjhlaksjdfh {useful()}')