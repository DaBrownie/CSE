class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job


class Programmer(Employee):
    def __init__(self, name, age, job, personal_computer):
        super(Programmer, self).__init__(name, age, job, personal_computer)
        self.personal_computer = personal_computer
