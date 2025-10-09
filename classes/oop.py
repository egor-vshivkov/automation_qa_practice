from abc import abstractmethod
import json


class Group:
    pupils = True
    school_name = 42
    director = 'MV'

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader


    def study(self):
        print('sit down and read')

    @abstractmethod
    def move(self):
        pass


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room

    def move(self):
        print('Run fast')


class HighGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('Go slowly')

class MediumGroup(Group):
    max_age = 15
    min_age = 10

first_a = PrimaryGroup('1 A', 15, 'SD', 112)
first_a.class_room = 1000000
print(first_a.class_room)

# data1.txt
{"Country": "Turkey", "avg_temp": 30}
# data2.txt
{"Country": "Greece", "avg_temp": 28}


def read_file(filename):
    file_data = open(filename, 'r')
    # data = file_data.read()
    data = json.load(file_data)
    file_data.close()
    return data

data1 = read_file('data1.txt')
data2 = read_file('data2.txt')

print(data1['Country'])
print(data1['avg_temp'])
print(data2['Country'])
print(data2['avg_temp'])


class CountryData:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self._comfort = self.__is_comfort()

    @property
    def data(self):
        return self.__data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self._comfort

    @comfort.setter
    def comfort(self, value):
        self._comfort = value

    def __read_file(self):
        file_data = open(self.__filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def __is_comfort(self):
        return self.__avg_temp > 25

    def __str__(self):
        return f'str File {self.__filename} with data {self.__data}'

    def __repr__(self):
        return f'repr File {self.__filename} with data {self.__data}'

    def __lt__(self, obj):
        return self.avg_temp < obj.avg_temp

    def __le__(self, obj):
        return self.avg_temp <= obj.avg_temp

    def __add__(self, obj):
        return [self, obj]

data1 = CountryData('data1.txt')
data1.comfort = False
print(data1.comfort)
# data1.data = 'skdfjhskdjf'
print(data1.data)
# data1.__data = {'1': 5}
print(data1.data)
print(data1.country)
# print(data1.avg_temp)
data2 = CountryData('data2.txt')
print(data2.country)
data1.__avg_temp = 2342342
print(data1.avg_temp)

# data3.txt
{"Country": "Poland", "avg_temp": 15, "min_temp": 2}


class CountryDataWithMinTemp(CountryData):
    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']


data3 = CountryDataWithMinTemp('data3.txt')
print(data3.avg_temp)
print(data3.min_temp)

print(data1)  # print(str(data1))
print(data1 < data2)
print(data1 <= data2)
print(data1 > data2)
print(data1 >= data2)
print(data1 + data2)


class MyClass:
    @property
    def my_word(self):
        return 'hello'

    def act(self):
        print('hello')


qqq = MyClass()
qqq.act()
qqq.my_word


class CountryData:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self._comfort = self.__is_comfort()

    @property
    def data(self):
        return self.__data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self._comfort

    @comfort.setter
    def comfort(self, value):
        self._comfort = value

    def __read_file(self):
        file_data = open(self.__filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def __is_comfort(self):
        return self.__avg_temp > 25


data1 = CountryData('data1.txt')
data1.comfort = False
print(data1.comfort)
# data1.data = 'skdfjhskdjf'
print(data1.data)
# data1.__data = {'1': 5}
print(data1.data)
print(data1.country)
# print(data1.avg_temp)
data2 = CountryData('data2.txt')
print(data2.country)
data1.__avg_temp = 2342342
print(data1.avg_temp)
