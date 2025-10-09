def calc():
    print(1 + 1)

calc()
print(calc)
new_calc = calc
print(new_calc)
new_calc()
a = 1


def greet():
    def hello():
        return 'hello'

    return hello()


print(greet())


def outer():
    def inner():
        result = 2 + 5
        return result

    return inner


print(outer()())
inner_function = outer()
print(inner_function())

def func1(give_me_a_func):
    print('before')
    give_me_a_func()
    print('after')


def simple1():
    print('simple1')

def simple2():
    print('simple2')

simple1()
simple2()

func1(simple1)
func1(simple2)

def simple3():
    print('I')
    print('love')
    print('Python')
    print('and')
    print('decorators')

func1(simple3)


def add_text(func):
    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper


def simple1():
    print('simple1')


simple1()

simple1 = add_text(simple1)

print(simple1)
simple1()


def simple2():
    print('simple2')


simple2()

simple2 = add_text(simple2)

simple2()

def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper


@add_text
def simple1():
    print('simple1')

@add_text
def simple2():
    print('simple2')
    print('simple2')

simple1() # add_text(simple1)()
simple2()


def add_logs(func):
    def wrapper():
        print(f'function {func.__name__} started')
        result = func()
        print(f'finished {func.__name__}')
        return result

    return wrapper


@add_logs
def simple1():
    print('simple1')


@add_logs
def simple2():
    print('simple2')
    print('simple2')


@add_logs
def print_nothing():
    return 'hello'


@add_logs
def calc(x):
    print(x * 2)


simple1()
simple2()
print(print_nothing())
calc(3)


def add_logs(func):
    def wrapper(*args):
        print(f'function {func.__name__} started')
        result = func(*args)
        print(f'finished {func.__name__}')
        return result

    return wrapper


@add_logs
def simple1():
    print('simple1')


@add_logs
def print_nothing():
    return 'hello'


@add_logs
def calc(x):
    print(x * 2)


@add_logs
def calc2(x, y):
    print(x * y)


simple1()
print(print_nothing())
calc(3)
calc2(3, 7)

def func(*args):
    # print((1, 2, 3, 5, 9))
    print(*args)
    # print(1, 2, 3, 5, 9)

func(1, 2, 3, 5, 9)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

new_list = []
# for x in my_list:
#     new_list.append(x * 2)
new_list = [x * 2 for x in my_list]
# new_list = map(lambda x: x * 2, my_list)


print(new_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# new_list = []
# for x in my_list:
#     if x % 2 == 0:
#         new_list.append(x)

# new_list = filter(lambda x: x % 2 == 0, my_list)
new_list = [x for x in my_list if x % 2 == 0]
new_list2 = [x if x % 2 == 0 else x + 1 for x in my_list]
new_list2 = [x if x % 2 == 0 else print(f'{x} is not even') for x in my_list]
new_generator = (x for x in my_list if x % 2 == 0)

print(new_list)
print(new_list2)
print(new_generator)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

{1: 3, 'SDFSDF': 'WER'}

# new_dict = {}
# for x in my_list:
#     new_dict[x] = x * 3

new_dict = {x: x * 3 for x in my_list}

print(new_dict)

data = [('one', 'two'), ('three', 'four')]

# new_dict = {}
# for key, value in data:
#     new_dict[key] = value

new_dict = {key: value for key, value in data}
new_dict = dict(data)

print(new_dict)

countries = ['USA', 'Hawaii', 'Cuba']
temps = [23, 33, 35]

country_temps_dict = dict(zip(countries, temps))
print(country_temps_dict)
