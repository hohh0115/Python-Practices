"""
class student:
    def __init__(self, name, score):
        self.student_name = name
        self.student_score = score
        print(self)
        print(self.__class__)

    def print_score_by_object(self):
        print('%s: %d' % (self.student_name, self.student_score))

    def grade_evaluation(self):
        if self.student_score >= 90:
            return 'A'
        elif self.student_score >= 60:
            return 'B'
        else:
            return 'C'

def print_score_by_func(student_object):
    print('%s: %d' % (student_object.student_name, student_object.student_score))

x = student('Howard', 100)
x.print_score_by_object()
print_score_by_func(x)
print(x.grade_evaluation())

lisa = student('Lisa', 89)
print(lisa.student_name, lisa.student_score, lisa.grade_evaluation(), sep=', ')
"""

class student_new:
    def __init__(self, name, score):
        self.__student_name = name
        # self.__student_score = score
        self.reset_student_score(score)

    def __str__(self):
        return 'hahaha'

    def get_student_name(self):
        return self.__student_name

    def get_student_score(self):
        return self.__student_score

    def reset_student_name(self, new_name):
        self.__student_name = new_name

    def reset_student_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__student_score = new_score
        else:
            raise ValueError('Bad Score')

x = student_new('Howard', 100)
print(x)
print(x._student_new__student_name)
print(x.get_student_name())
print(x.get_student_score())
x.reset_student_name('Andy')
x.reset_student_score(44)
print(x.get_student_name())
print(x.get_student_score())

x.__student_name = 'Lisa'
print(x.__student_name)
print(x.get_student_name())


"""
class Animal:
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass

def run_twice(animal):
    animal.run()
    animal.run()

x = Dog()
x.run()

y = Cat()
y.run()

run_twice(Cat())
run_twice(Dog())

class Timer:
    def run(self):
        print('Start...')

run_twice(Timer())
"""

"""
class Animal:
    def run(self):
        print('Animal is running...')

# list = list(range(10))
# print(dir(list))
x = 'ABCDE123'
print(dir(x))
print(x.__getattribute__('__init__'))
print(x)
# print(dir(Animal))
"""