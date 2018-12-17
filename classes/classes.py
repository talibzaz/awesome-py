import datetime

class Person:
    continent = 'Europe'

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_fullName(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @classmethod
    def get_continent_abbr(cls):
        abbr = cls.continent[:2].upper()
        return abbr

    @staticmethod
    def get_now():
        return datetime.datetime.now()

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    jon = Person('John', 'Doe', 'ohn@doe.com')
    full_name = jon.get_fullName()
    print(full_name)
    print(jon.get_continent_abbr())
    print(Person.get_now())

    buzz = Dog('buzz')
    tom = Dog('tommy')

    buzz.add_tricks('can roll over')
    tom.add_tricks('can swim')
    buzz.age = 15

    print(buzz.tricks)
    print(buzz.age)
    print(tom.tricks)
